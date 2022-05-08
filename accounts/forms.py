from dataclasses import field
from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
    
    def __int__(self, *args, **kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget_attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget_attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget_attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget_attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget_attrs['class'] = 'form-control'