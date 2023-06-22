from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class ShopView(View):
    def get(self, request):
        context = {'data': [
            {'name': 'Bell Pepper',
             'discount': 30,
             'price_before': 120.00,
             'price_after': 80.00,
             'url': 'store/images/product-1.jpg'
             },
            {'name': 'Strawberry',
             'discount': None,
             'price_before': 120.00,
             'url': 'store/images/product-2.jpg'},
            {'name': 'Green Beans',
             'discount': None,
             'price_before': 120.00,
             'url': 'store/images/product-2.jpg'}
        ]}
        return render(request, 'store/shop.html', context)

class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')

class ProductSingleView(View):
    def get(self, request):
        return render(request, 'store/product-single.html')