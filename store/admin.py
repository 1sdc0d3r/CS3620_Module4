from django.contrib import admin
from .models import Product, Category, Tag

# class inlineTagModel(admin.StackedInline): # or TabularInline
#     model = Tag
#     extra = 1

class TagInline(admin.TabularInline):
    model = Product.tags.through
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    inlines = [TagInline]
    exclude = ("tags",) #required with through??


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)

class TagAdmin(admin.ModelAdmin):
    # list_filter = ("tag",)
    list_display = ("tag",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Tag)
