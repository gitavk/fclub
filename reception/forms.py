# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

from models import *

class FormReminder(ModelForm):
    class Meta:
        model = Reminder

class FormGuest(ModelForm):
    class Meta:
        model = Guest