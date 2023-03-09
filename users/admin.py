from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import skills


admin.site.register(Profile)
admin.site.register(skills)
