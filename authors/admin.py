from django.contrib import admin
from authors.models import Authors

# Register your models here.

@admin.register(Authors)
class AuthorModelAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'birthday_year')
    list_display = ('first_name', 'last_name', 'birthday_year')
    list_filter = ('last_name',)
    ordering = ('-birthday_year',)

