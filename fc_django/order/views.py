from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.utils.decorators import method_decorator
from django.db import transaction

from fc_user.decorators import login_required
from fc_user.models import FcUser
from .models import Order
from .forms import RegisterForm
from product.models import Product

# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        # 트랜잭션 : 하나의 단위, 일련의 여러 동작을 하나의 동작으로 처리 - 전체가 성공하면 성공, 하나라도 실패하면 전체 실패
        # @transaction.atomic() : 장고에서 제공하는 atomic() 함수, 데코레이터로 함수 위에 붙이면 함수 전체에 적용
        # with 안의 내용 전부 트랜잭션으로 처리
        with transaction.atomic():
            product = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=product,
                fc_user=FcUser.objects.get(email=self.request.session.get('user'))
            )
            order.save()

            # 상품의 재고 차감
            product.stock -= int(form.data.get('quantity'))
            product.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        """ 기존 form 생성할때 request 인자값 함께 전달해서 form클래스 생성 """
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    # model = Product # 자기가 주문한 정보만 보여야 돼서 이렇게 하면 안됨
    template_name = 'order/order.html'
    context_object_name = 'order_list'
    
    def get_queryset(self, **kwargs):
        # self.request 가져오기 위해서 get_queryset 오버라이딩
        queryset = Order.objects.filter(fc_user__email=self.request.session.get('user'))
        return queryset



