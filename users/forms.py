

from users import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from.models import Profile, skills, Message


class editForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image', 'social_github', 'social_twitter'

                  ]


class skill(ModelForm):
    class Meta:
        model = skills
        fields = ['name', 'description']


class formmessage(ModelForm):
    class Meta:
        model = Message

        fields = ['subject', 'body']
