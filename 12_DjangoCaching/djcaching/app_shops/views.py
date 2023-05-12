from django.shortcuts import render
from django.views.generic import DetailView, ListView
from app_shops.models import Shop, Product
from cart.forms import CartAddProductForm


def page_with_cached_fragments(request):
    shops = Shop.objects.all()
    return render(request, 'app_shops/page_with_cached_fragments.html', context={
        'shops': shops
    })


class ProductDetailsView(DetailView):
    template_name = 'app_shops/product-details.html'
    queryset = Product.objects
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm()
        return context


class ProductsListView(ListView):
    template_name = 'app_shops/products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
