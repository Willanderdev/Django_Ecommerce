from django.shortcuts import render

from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from .forms import UserAdminCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
# se a view for baseada em função vc usa esse abaixo
#from django.contrib.auth.decorators import login_required


from . models import User


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'accounts/update_user.html'
    fields = ['username', 'name', 'email']
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user


class UpdateePasswordview(LoginRequiredMixin, FormView):
    
    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('index')
    form_class = PasswordChangeForm
    
    def get_form_kwargs(self):
        kwargs = super(UpdateePasswordview, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    