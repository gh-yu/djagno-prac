from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.
from fc_user.forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.email

        return super().form_valid(form)


