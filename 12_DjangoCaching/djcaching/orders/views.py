from django.db import transaction, IntegrityError
from django.shortcuts import render

from app_shops.models import Shop
from app_users.models import Balance
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            try:
                order = order_transaction(user_id=request.user.id, form=form, cart=cart)
                return render(request, 'orders/order/created.html',
                              {'order': order})
            except IntegrityError as Error:
                return render(request, 'orders/order/create.html',
                              {'cart': cart, 'form': form, 'error': 'error creating order ' + str(Error)})

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


# def reduce_stock(product_id, shop_id, amount):
#     stock = ShopStock.objects.get(product_id=product_id, shop_id=shop_id)
#     if stock.stock >= amount:
#         stock.stock -= amount
#         stock.save()
#     else:
#         raise IntegrityError("not enough product in stock")


# @transaction.atomic
# def order_transaction(user_id: int, form: OrderCreateForm, cart: Cart) -> Order:
#     """Использование atomic как менеджер контекста"""
#
#     try:
#         with transaction.atomic():
#             reduce_user_balance(user_id, cart.get_total_price())
#             form.created_by = User.objects.get(pk=user_id)
#             order = form.save()
#             for item in cart:
#                 shop = Shop.objects.get(pk=item['shop'])
#                 reduce_stock(item['product'].id, shop.id, item['shop_quantity'])
#                 OrderItem.objects.create(order=order,
#                                          product=item['product'],
#                                          price=item['price'],
#                                          quantity=item['shop_quantity'],
#                                          shop=shop
#                                          )
#
#     except IntegrityError as Error:
#         raise Error
#
#     cart.clear()
#     return order
