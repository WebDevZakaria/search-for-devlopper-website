from django.contrib import admin

# Register your models here.
from .models import Tag, project, Reviews, formation


admin.site.register(project)
admin.site.register(Reviews)
admin.site.register(Tag)
admin.site.register(formation)
