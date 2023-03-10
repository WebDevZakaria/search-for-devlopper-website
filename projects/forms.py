from projects import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from.models import project, formation, Reviews


class projectform(ModelForm):
    class Meta:
        model = project
        fields = ['title', 'description', 'featured_image',
                  'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(projectform, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Add title'})

        self.fields['description'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Add  description'})
        self.fields['demo_link'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Add  link'})
        self.fields['source_link'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Add  link'})


class formationform(ModelForm):
    class Meta:
        model = formation
        fields = ['username', 'password']


class formuser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2', 'email']


class formreview(ModelForm):
    class Meta:
        model = Reviews
        fields = ['value', 'body']
