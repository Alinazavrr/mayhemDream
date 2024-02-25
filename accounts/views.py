from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.apps import apps
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import logout
from django.urls import reverse 

from .forms import SignUpForm

# Create your views here.

# class LoginView(FormView)
# GET - отдает форму с запросом логина и пароля
# POST - генерирует сессию: отдавая ее ползователю





class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/delete_account.html'
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.success_url)



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main:main_page')
    template_name = 'accounts/signup.html'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next' # default
    extra_context = {'key': 'value'}
    authentication_form = AuthenticationForm # default


def my_logout(request):
    logout(request)
    return redirect(reverse('home_page'))

# LogoutView(TemplateView)
# class UserLogoutView(LogoutView):
#     template_name = 'accounts/logout.html'
#     # next_page =
#     redirect_field_name = 'next'
#     extra_context = {}


# PasswordChangeView(FormView)
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    # success_url = reverse('password_change_done') default
    extra_context = {}
    # form_class = PasswordChangeForm default


# PasswordChangeDoneView(TemplateView)
class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    extra_context = {} # title


class UserPermissions(TemplateView):
    template_name = 'accounts/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ваши разрешения'
        context['data'] = self.request.user.get_all_permissions()
        return context

