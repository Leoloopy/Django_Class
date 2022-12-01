from django.contrib import admin
from .models import Publisher, Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'publisher']
    list_editable = ['isbn']
    list_filter = ['publisher', 'date_published']
    search_fields = ['title__istartswith', 'isbn__exact']
    date_hierarchy = 'date_published'


admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
