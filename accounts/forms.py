from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز عبور',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']

    def cleanpassword(self):
        cd =self.cleaned_data
        if cd['password'] != cd['password']:
            raise forms.ValidationError('رمزها یکسان نمی باشند')
        return cd['password2']