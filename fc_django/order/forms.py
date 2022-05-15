from django import forms

from fc_user.models import FcUser
from product.models import Product
from .models import Order


class RegisterForm(forms.Form):
    
    # forms.py에서 request 활용하기 위한 생성자
    # form객체 생성하면서 request 넣고 초기화
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        }, label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입력해주세요.'
        }, label='상품', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fc_user = self.request.session.get('user')

        if not (quantity and product and fc_user):
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
