from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"article/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom = models.CharField(max_length=100)
    main_picture = models.ImageField(_("main_picture"), upload_to=upload_to)
    main_description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    buy_link = models.CharField(max_length=300)
    price = models.FloatField(null=True, blank=True)
    # ---------------------------------------------------------------------- #
    video_link = models.CharField(max_length=300, null=True, blank=True)
    second_picture = models.ImageField(_("second_picture"), upload_to=upload_to, null=True, blank=True)
    second_description = models.TextField(null=True, blank=True)
    third_picture = models.ImageField(_("third_picture"), upload_to=upload_to, null=True, blank=True)
    third_description = models.TextField(null=True, blank=True)
    fourth_picture = models.ImageField(_("fourth_picture"), upload_to=upload_to, null=True, blank=True)
    fourth_description = models.TextField(null=True, blank=True)
    fifth_picture = models.ImageField(_("fifth_picture"), upload_to=upload_to, null=True, blank=True)
    fifth_description = models.TextField(null=True, blank=True)
    sixth_picture = models.ImageField(_("sixth_picture"), upload_to=upload_to, null=True, blank=True)
    sixth_description = models.TextField(null=True, blank=True)
    features = models.TextField()

    def __str__(self):
        return self.nom