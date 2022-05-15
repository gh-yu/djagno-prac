from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

# Create your views here.
from fc_user.forms import RegisterForm, LoginForm
from fc_user.models import FcUser


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        fc_user = FcUser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        fc_user.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')