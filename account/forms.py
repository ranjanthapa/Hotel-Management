from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError

from .models import Account


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

        self.fields["first_name"].widget.attrs["placeholder"] = "Enter your first name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter your last name"
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Enter your phone number"

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Enter Password",
        "class": "form-control",
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Confirm Password",
        "class": "form-control",
    }))

    class Meta:
        model = Account
        fields = ["first_name", "last_name", "email", "phone_number"]

    def clean(self):
        cleaned_data = super().clean()
        first_password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if first_password != confirm_password:
            raise ValidationError("Password don't match")
        return cleaned_data
