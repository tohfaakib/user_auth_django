from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')


class CustomSignupForm(SignupForm):
    age = forms.IntegerField(label="Age", widget=forms.TextInput(attrs={"type": "integer", "placeholder": "Age"}),)
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.age = self.cleaned_data['age']
        user.save()
        return user
