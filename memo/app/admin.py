from django.contrib import admin

# Register your models here.
from .models import Memo

class MemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

admin.site.register(Memo, MemoAdmin)