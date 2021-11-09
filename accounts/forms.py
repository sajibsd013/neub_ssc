from django import forms
from blood_app.models import Blood_donor


class Sign_in(forms.Form):
    username = forms.CharField(max_length=122, widget=forms.TextInput(
        attrs={
            'placeholder': "Enter your username",
            'class': 'form-control mb-3'
        }
    ))
    password = forms.CharField(max_length=122, widget=forms.PasswordInput(
        attrs={
            'placeholder': "Enter your Password",
            'class': 'form-control mb-4'
        }
    ))




class Sing_up(forms.Form):

    username = forms.CharField(max_length=122, widget=forms.TextInput(
        attrs={
            'placeholder': "Enter your username",
            'class': 'form-control'
        }
    ))

    password1 = forms.CharField(max_length=122, widget=forms.PasswordInput(
        attrs={
            'placeholder': "Enter your Password",
            'class': 'form-control'
        }
    ))

    password2 = forms.CharField(max_length=122, widget=forms.PasswordInput(
        attrs={
            'placeholder': "Enter your Password",
            'class': 'form-control '
        }
    ))

class user_rei_form(forms.ModelForm):
    class Meta:
        model = Blood_donor
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Enter your name",'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': "Enter your email",'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'blood_type': forms.Select(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control','placeholder':'Select a Date','type':'date'}),
            'last_donate': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'address': forms.Textarea(attrs={'cols': 40, 'rows': 3, 'class': 'form-control'}),
        }
