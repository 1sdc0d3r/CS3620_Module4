from django.contrib import admin
from .models import Product, Category, Tag

class inlineTagModel(admin.StackedInline): # or TabularInline
    model = Tag
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ("categoryy",)
    # inlines = [inlineTagModel]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

class TagAdmin(admin.ModelAdmin):
    list_filter = ("tags",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tag, TagAdmin)
admin.site.register(Tag)
