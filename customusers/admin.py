from django.contrib import admin
from customusers.models import CustomUsers

@admin.register(CustomUsers)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('last_name',)
    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('-username',)

