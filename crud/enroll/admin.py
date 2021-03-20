from django.contrib import admin
from .models import crud
# Register your models here.
@admin.register(crud)
class crudadmin(admin.ModelAdmin):
    list_display=('id','title','key','desc')