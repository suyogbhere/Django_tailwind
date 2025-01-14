from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User



class signup(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True'}),label='Password (Confirm)')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True}),
                'first_name':forms.TextInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True}),
                'last_name':forms.TextInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True}),
                'email':forms.EmailInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True})}

        labels={'email':'Email'}





# class LoginForm(AuthenticationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-input rounded-lg border-gray-300 shadow-sm focus:ring-indigo-500 focus:border-indigo-500","autofocus":True}))

