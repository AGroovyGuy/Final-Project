"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from project.views import (LoginView, CreateAccountView,
                           HubView, LogoutView,
                            ForumView, SettingsView,
                           ContactView, CategoriesView,
                           RandomView, JelitoView,
                           DeleteView, AddView,
                           DeleteAnotherView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^createuser', CreateAccountView.as_view(), name="createaccount"),
    url(r'^logout', LogoutView.as_view(), name="logout"),
    url(r'^hub', HubView.as_view(), name="hub"),
    url(r'^categories/(?P<id>(\d)+)', CategoriesView.as_view(), name="tymczasowy"),
    url(r'^forum', ForumView.as_view(), name="forum"),
    url(r'^settings/$', SettingsView.as_view(), name="settings"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^random/(?P<id>(\d)+)', RandomView.as_view(), name="randomsubpage"),
    url(r'^jelito/', JelitoView.as_view(), name="randomjelito"),
    url(r'^delete/(?P<id>(\d)+)', DeleteView.as_view(), name="delete"),
    url(r'^del/(?P<id>(\d)+)', DeleteAnotherView.as_view(), name="deleteanother"),
    url(r'^add/(?P<id>(\d)+)', AddView.as_view(), name="add"),

]
