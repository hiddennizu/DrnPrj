from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username or Email :',
        widget=forms.TextInput(attrs={'class': 'form-control custom-form', 'placeholder': 'Username or Email :'}),
    )

    password = forms.CharField(
        label='Password ',
        widget=forms.PasswordInput(attrs={'class': 'form-control custom-form', 'placeholder': 'Password :'}),
        strip=False,
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = None
        if user:
            return user.username
        return None


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-form', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={'class': 'form-control custom-form', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control custom-form', 'placeholder': 'Enter your Username'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control custom-form', 'placeholder': 'Enter your Firstname'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control custom-form', 'placeholder': 'Enter your Surname'}),
            'email': forms.TextInput(attrs={'class': 'form-control custom-form', 'placeholder': 'Enter Email Addess '}),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if len(cd['password'] and cd['password2']) < 8:
            raise forms.ValidationError('must be 8 chars long')

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class password_change_form(forms.Form):
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your current password'}),
        strip=False
    )

    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your new password'}),
        strip=False
    )

    confirm_new_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
        strip=False
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(password_change_form, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data["current_password"]
        if not self.user.check_password(current_password):
            raise forms.ValidationError('Incorrect Current Password')
        return current_password

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']
        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise forms.ValidationError('Password Mismatch')
        password_validation.validate_password(confirm_new_password, self)
        return confirm_new_password

    def save(self, commit=True):
        password = self.cleaned_data['confirm_new_password']
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class ProfileForm(forms.ModelForm):
    """
    Form to edit user Profile
    """

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff'

        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }
