from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User
from .models import Genre


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    top_genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = User
        fields = ("date_of_birth", "username", "first_name", "last_name", "email", "password1", "password2", "top_genres")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.top_genres.set(self.cleaned_data['top_genres'])
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



