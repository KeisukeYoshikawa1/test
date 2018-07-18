from django.contrib import admin
from item.models.model_file import Item

# admin.site.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    list_display_links = ('id', )

admin.site.register(Item, ItemAdmin)