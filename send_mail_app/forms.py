from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class NewUserForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    email=forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'})) 

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        # Debugging print statement to see the email and its count of alphabets
        # print("Email:", email, "Alphabet count:", sum(c.isalpha() for c in email))
        
        # if sum(c.isalpha() for c in email) < 6:
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            raise ValidationError('Email must have at least 6 alphabets.')
        
        return email

# class NewLoginForm(AuthenticationForm):
#     email=forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
#     password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
#     class Meta:
#         fields=['password1','email']
        
class NewLoginForm(AuthenticationForm):
    
    username = forms.CharField(label='Username', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

    # class Meta:
    #     model = User
    #     fields = ['email','password1']    
    # Create your forms here.

# class NewUserForm(UserCreationForm):
    
# 	email = forms.EmailField(required=True)
# 	class Meta: 
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
