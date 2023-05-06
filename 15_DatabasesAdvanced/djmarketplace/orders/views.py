from django.db import transaction, IntegrityError
from django.shortcuts import render

from app_shop.models import Shop, ShopStock
from app_users.models import Balance
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():

            order = order_transaction(user_id=request.user.id, form=form, cart=cart)
            if order:
                return render(request, 'orders/order/created.html',
                              {'order': order})
            else:
                return render(request, 'orders/order/create.html',
                              {'cart': cart, 'form': form, 'error': 'error creating order'})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


def reduce_user_balance(user_id, order_size):
    balance = Balance.objects.get(user=user_id)
    print(balance.amount)
    if order_size <= balance.amount:
        balance.amount -= order_size
        balance.save()
    else:
        raise IntegrityError("not enough money")


def reduce_stock(product_id, shop_id, amount):
    stock = ShopStock.objects.get(product_id=product_id, shop_id=shop_id)
    if stock.stock >= amount:
        stock.stock -= amount
        stock.save()
    else:
        raise IntegrityError("not enough product in stock")


@transaction.atomic
def order_transaction(user_id, form, cart):
    """Использование atomic как менеджер контекста"""

    try:
        with transaction.atomic():
            reduce_user_balance(user_id, cart.get_total_price())

            order = form.save()
            for item in cart:
                shop = Shop.objects.get(pk=item['shop'])
                reduce_stock(item['product'].id, shop.id, item['shop_quantity'])
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['shop_quantity'],
                                         shop=shop
                                         )

    except IntegrityError:
        return False

    cart.clear()
    return order
