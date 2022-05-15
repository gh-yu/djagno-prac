from django import forms
from django.contrib.auth.hashers import check_password

from .models import FcUser


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )
    re_password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호 확인'
    )

    # clean함수는 유효성 검사만 서비스 로직(모델 데이터 저장 등)은 view에
    def clean(self):
        cleand_data = super().clean()
        email = cleand_data.get('email')
        password = cleand_data.get('password')
        re_password = cleand_data.get('re_password')

        if email and password and re_password:
            if password != re_password:
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleand_data = super().clean()
        email = cleand_data.get('email')
        password = cleand_data.get('password')

        if email and password:
            try:
                fc_user = FcUser.objects.get(email=email)
            except FcUser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return

            if not check_password(password, fc_user.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')
            # else:
                # self.email = fc_user.email

