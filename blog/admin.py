from django.contrib import admin
from .models import Post, Category, Comment, PostViews

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_to_str', 'publish', 'status', 'get_view_count')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    def category_to_str(self, obj):
        Category = [category.title for category in obj.category.all()]
        return ', '.join(Category)
    category_to_str.short_description = 'category'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostViews)