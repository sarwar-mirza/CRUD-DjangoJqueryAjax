from django import forms
from .models import User

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        
        labels = {
            'email': 'Email',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control", "id":"nameid", "placeholder":"name"}),
            'email': forms.EmailInput(attrs={"class":"form-control", "id":"emailid", "placeholder":"Email"}),
            'password': forms.PasswordInput(attrs={"class":"form-control", "id":"passwordid", "placeholder":"Password"}),
        }