from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class PostAdmin(admin.ModelAdmin):
    # tener mucho cuidado con las many-to-many (categories)
    readonly_fields = ('created', 'update')
    # abajo en la tupla no se puede simplemente poner 'categories'
    list_display = ('title', 'author', 'published', 'post_categories') # solución many-to-many
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    # solución para las many-to-many
    def post_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)