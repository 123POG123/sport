from django.contrib import admin

# Register your models here.
from sport.models import MyForm

admin.site.site_header = 'news'
admin.site.register(MyForm)