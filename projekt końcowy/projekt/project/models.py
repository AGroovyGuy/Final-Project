from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return self.category


class Passtime(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ForumPost(models.Model):
    contents = models.TextField()
    postdate = models.DateTimeField(auto_now=True)
    op = models.ForeignKey(User, on_delete=models.CASCADE)


COLOR = (
    ("black", "czarny"),
    ("white", "biały"),
    ("red", "czerwony"),
    ("yellow", "żółty"),
    ("blue", "niebieski"),
)


FONT_COLOR = (
    ("black", "czarny"),
    ("white", "biały"),
    ("red", "czerwony"),
    ("yellow", "żółty"),
    ("blue", "niebieski"),
    ("#706969", "piękna szarość")
)

FONT_SIZE = (
    ("12px", "Zupełnie normalna"),
    ("9px", "Nikczemnych rozmiarów"),
    ("15px", "Potężnej postury"),
    ("18px", "Ogromna do przesady"),
)


class RandomSubPage(models.Model):
    hyperlink = models.CharField(max_length=400)
    subpage = models.ForeignKey(Passtime, on_delete=models.CASCADE)


class JelitoButton(models.Model):
    url = models.CharField(max_length=400)

