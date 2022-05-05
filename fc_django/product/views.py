from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView

from .forms import RegisterForm
from .models import Product


# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product/product.html'


# class ProductCreate(FormView):
#     template_name = 'product/register_product.html'
#     form_class = RegisterForm
#
#     def form_valid(self, form):
#         print("fadfadfa")
#         Product.objects.create(
#             name=form.data.get('name'),
#             price=form.data.get('price'),
#             description=form.data.get('description'),
#             stock=form.data.get('stock')
#         )
#
#         return super().form_valid(form)

class ProductCreate(FormView):
    template_name = 'product/register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    template_name = 'product/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'




