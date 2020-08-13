# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.db import models
import datetime
import time

from django.urls import reverse
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from mapbox_location_field.models import LocationField
from mapbox_location_field.forms import AddressAutoHiddenField
from phone_field.templatetags.phone import raw_phone
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import get_thumbnail

def upload_avatar(self, filename):
    # verification de l'extension
    real_name, extension = os.path.splitext(filename)
    name = str(int(time.time())) + extension
    return "avatars/" + "user.username.jpeg"

def upload_profile(self, filename):
    # verification de l'extension
    real_name, extension = os.path.splitext(filename)
    name = str(int(time.time())) + extension
    return "profiles/" + "user.username.jpeg"

GENRE = (
    ('H', 'HOMMME'),
    ('F', 'FEMME'),
)

EXPERIENCE = (
    ('debutant', 'DEBUTANT'),
    ('intermediaire', 'INTERMEDIAIRE'),
    ('expert', 'EXPERT'),
)

class Langage(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['titre']

    def __str__(self):
        return self.titre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=10, verbose_name="GENRE", choices=GENRE, default="H")
    #status = models.CharField(max_length=50, verbose_name="Expérience", choices=EXPERIENCE)
    experence = models.CharField(max_length=50, choices=EXPERIENCE)
    wht = PhoneNumberField(help_text="+225xxxxxxxx", verbose_name="Contact WhatsApp") # PhoneNumber.from_string(phone_number=raw_phone, region='CI').as_e164
    pays = CountryField(blank_label='(Préciser Le Pays)')
    ville = models.CharField(max_length=255)
    langages = models.ManyToManyField(Langage, verbose_name="Preciser vos Langages")
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="upload_avatar", blank=True, null=True)
    profile = models.ImageField(upload_to="upload_profile", blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    add_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)
    # active = models.BooleanField(default=False)

    def __str__(self):
        if self.user.last_name or self.user.first_name:
            return '%s %s (%s)' %(self.user.last_name, self.user.first_name, self.experence)
        else:
            return self.user.username

    def get_absolute_url(self):
        return reverse('abonne:detail', args=[self.pk])

    class Meta:
        ordering = ('-add_le', '-update_le')

    def Avatar(self):
        if self.avatar:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.avatar.url)
        else:
            return "Aucune photo"

    Avatar.short_description = 'Avatar'

    def Profile(self):
        if self.profile:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.profile.url)
        else:
            return "Aucun Profile"

    Profile.short_description = 'Profile'

    class Meta:
        verbose_name_plural = "ABONNES"
        verbose_name = "abonne"



# Create your models here.
