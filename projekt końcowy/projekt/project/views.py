from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Avg
from .forms import (LoginForm, CreateAccountForm, AddForumPostForm, BackgroundColor,
                    AddSomething, RandomSubPageForm)
from .models import (Passtime, Categories, ForumPost, RandomSubPage, JelitoButton)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import UserPassesTestMixin
import hashlib


# Create your views here.

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "form-show.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            password = form.cleaned_data["password"]
            auth = authenticate(username=nickname, password=password)
            if auth:
                login(request, auth)
                return HttpResponseRedirect('/hub')
            else:
                return HttpResponse("Błędny login lub hasło.")
        return render(request, "form-show.html", {"form": form})


class CreateAccountView(View):
    def get(self, request):
        form = CreateAccountForm()
        return render(request, "form-show.html", {"form": form})

    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["nickname"]).count() > 0:
                messages.info(request, 'Istnieje już użytkownik o takim nicku.')
                return HttpResponseRedirect('/createuser')
            elif User.objects.filter(email=form.cleaned_data["mail"]).count() > 0:
                messages.info(request, 'Konto o podanym mailu już istnieje.')
                return HttpResponseRedirect('/createuser')
            User.objects.create_user(username=form.cleaned_data["nickname"],
                                                 password=form.cleaned_data["password"],
                                                 email=form.cleaned_data["mail"])
            return HttpResponseRedirect('/')


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


@method_decorator(login_required, name='dispatch')
class HubView(View):
    def get(self, request):
        categories = Categories.objects.all()
        ctx = {"categories": categories}
        return render(request, "hub.html", ctx)


@method_decorator(login_required, name='dispatch')
class CategoriesView(View):
    def get(self, request, id):
        categories = Categories.objects.get(pk=id)
        passtime_list = categories.passtime_set.all()
        ctx = {
            "passtimelist": passtime_list,
            "id": id,
        }
        return render(request, "categories.html", ctx)


@method_decorator(login_required, name='dispatch')
class RandomView(View):
    def get(self, request, id):
        passtime = Passtime.objects.get(pk=id)
        try:
            random = passtime.randomsubpage_set.order_by('?')[0]
            return HttpResponseRedirect(random.hyperlink)
        except IndexError:
            messages.info(request, 'To nie jest gatunek muzyki. Przemyśl swoje decyzje życiowe.')
            return HttpResponseRedirect(reverse("tymczasowy", args=[passtime.category.id]))


@method_decorator(login_required, name='dispatch')
class ForumView(View):
    def get(self, request):
        form = AddForumPostForm()
        ctx = {"posts": ForumPost.objects.all().order_by("-postdate"), "form": form}
        return render(request, "forum.html", ctx)

    def post(self, request):
        form = AddForumPostForm(request.POST)
        ctx = {"posts": ForumPost.objects.all().order_by("-postdate"), "form": form}
        if form.is_valid():
            contents = ForumPost.objects.create(contents=form.cleaned_data["contents"],
                                            op=self.request.user)
        return render(request, "forum.html", ctx)


@method_decorator(login_required, name='dispatch')
class SettingsView(View):
    def get(self, request):
        form = BackgroundColor()
        ctx = {"form": form}
        return render(request, "settings.html", ctx)

    def post(self, request):
        form = BackgroundColor(request.POST)
        if form.is_valid():
            color = form.cleaned_data["background"]
            fontcolor = form.cleaned_data["fontcolor"]
            size = form.cleaned_data["fontsize"]
            request.session['fontcolor'] = fontcolor
            request.session['background'] = color
            request.session['fontsize'] = size
            return HttpResponseRedirect('/settings')


@method_decorator(login_required, name='dispatch')
class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")


@method_decorator(login_required, name='dispatch')
class JelitoView(View):
    def get(self, request):
        button = JelitoButton.objects.order_by('?')[0]
        return HttpResponseRedirect(button.url)


@method_decorator(login_required, name='dispatch')
class DeleteView(View):
    def get(self, request, id):
        object = get_object_or_404(ForumPost, pk=id)
        object.delete()
        return HttpResponseRedirect('/forum')


@method_decorator(login_required, name='dispatch')
class AddView(View):
    def get(self, request, id):
        categories = Categories.objects.get(pk = id)
        passtime_list = categories.passtime_set.all()
        form = AddSomething()
        form2 = RandomSubPageForm()
        ctx = {
            "form": form,
            "form2": form2,
        }
        return render(request, "addstuff.html", ctx)

    def post(self, request, id):
        form = AddSomething(request.POST)
        form2 = RandomSubPageForm(request.POST)
        categories = Categories.objects.get(pk=id)
        if form.is_valid():
            Passtime.objects.create(name=form.cleaned_data["name"],
                                    category=categories)
            return HttpResponseRedirect(reverse("tymczasowy", args=[id]))
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse("tymczasowy", args=[id]))


@method_decorator(login_required, name='dispatch')
class DeleteAnotherView(View):
    def get(self, request, id):
        object = get_object_or_404(Passtime, pk=id)
        category_id = object.category.id
        object.delete()
        return HttpResponseRedirect(reverse("tymczasowy", args=[category_id]))





