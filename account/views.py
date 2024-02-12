from django.contrib import messages, auth
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm
from .models import Account


class SigInView(LoginView):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'account/login.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('room:home')
        else:
            messages.error(request, 'Wrong credential')
            return render(request, 'account/login.html')


class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_message = "Account created successfully. You can now log in."
    success_url = reverse_lazy('account:login')

    def form_invalid(self, form):
        messages.error(self.request, "Password Doesn't match")
        return super().form_invalid(form)

    def form_valid(self, form):
        try:
            print(form)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.user_name = form.cleaned_data['email'].split('@')[0]
            user.is_active = True
            user.save()
            return super().form_valid(form)

        except IntegrityError:
            messages.error(self.request, 'User with the given email exists')
            return super().form_invalid(form)


def sign_out(request):
    auth.logout(request)
    return redirect("room:home")


