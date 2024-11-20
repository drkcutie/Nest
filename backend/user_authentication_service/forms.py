from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


User = get_user_model()


#use this for login
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

#use this for registering the user
# class RegisterForm(forms.ModelForm):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password']
#         widgets = {
#             'password': forms.PasswordInput
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
     
        if password and len(password) < 8:
            print("Password must be at least 8 characters long.")
            
            raise forms.ValidationError("Password must be at least 8 characters long.")

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving the user
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

