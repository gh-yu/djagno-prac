from django.shortcuts import redirect

from fc_user.models import FcUser


def login_required(function):  # 호출할 함수를 매개변수로 받음
    def wrapper(request, *args, **kwargs):  # 호출할 함수를 감싸는 함수
        user = request.session.get('user')
        if not user:
            return redirect('/login')
        return function(request, *args, **kwargs)  # 매개변수로 받은 함수를 호출

    return wrapper  # wrapper 함수 반환


def admin_required(function):
    def wrapper(request, *args, **kwargs):
        user = request.session.get('user')
        if not user:
            return redirect('/login')

        user = FcUser.objects.get(email=user)
        if user.level != 'admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrapper
