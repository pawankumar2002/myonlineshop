from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register((Product,Orders))
admin.site.site_header = "myonlineshop Dashboard"
