from django import forms
from .models import (Passtime, Categories, COLOR, FONT_COLOR,
                     FONT_SIZE, RandomSubPage)
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=150,  label="nickname")
    password = forms.CharField(max_length=150,  label="Hasło", widget=forms.PasswordInput)


class CreateAccountForm(forms.Form):
    nickname = forms.CharField(max_length=100, label="Nickname")
    password = forms.CharField(max_length=150, label="Hasło", widget=forms.PasswordInput)
    mail = forms.CharField(max_length=150, label="E-mail")


class AddForumPostForm(forms.Form):
    contents = forms.CharField(label="Czym chcesz się podzielić?", widget=forms.Textarea)


class BackgroundColor(forms.Form):
    background = forms.ChoiceField(label="Kolor tła:",
                                   choices=COLOR)

    fontcolor = forms.ChoiceField(label="Kolor fontu:",
                                  choices=FONT_COLOR)

    fontsize = forms.ChoiceField(label="Rozmiar czcionki;",
                                 choices=FONT_SIZE)


class AddSomething(forms.Form):
    name = forms.CharField(max_length=64, label="Dodaj nazwę:")


class RandomSubPageForm(forms.ModelForm):
    class Meta:
        model = RandomSubPage
        fields = ['hyperlink', 'subpage']