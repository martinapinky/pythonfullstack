from django.contrib import admin
from .models import Painting, Category

# Register your models here.
admin.site.register(Painting)
admin.site.register(Category)

admin.site.site_header = "Core Admininstration"
admin.site.site_title = "Core Admin Portal"