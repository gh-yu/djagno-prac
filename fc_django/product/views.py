from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, DetailView

from fc_user.decorators import admin_required
from .forms import RegisterForm
from .models import Product
from order.forms import RegisterForm as OrderForm

# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product/product.html'


@method_decorator(admin_required, name='dispatch')
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

    # 상세 페이지에 내가 원하는 데이터 넘길 수 있도록 추가 (오버라이딩)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = OrderForm(self.request)
        return context

