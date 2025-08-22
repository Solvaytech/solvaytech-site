from django.contrib import admin
from .models import Product, Article
from .models import Project

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    fields = (
        'name', 'description', 'link', 'datasheet',
        'image1', 'image2', 'image3', 'created_at'
    )
    
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('title', 'created_at')
    fields = ('title', 'content', 'link', 'created_at')

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('title', 'created_at')
    fields = ('title', 'description', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Project, ProjectAdmin)