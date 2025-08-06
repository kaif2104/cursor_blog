from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'updated_date')
    list_filter = ('created_date', 'updated_date', 'author')
    search_fields = ('title', 'content', 'author__username')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
