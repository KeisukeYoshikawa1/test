import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
items = Item.objects.all().order_by('name', '-price')
for item in items:
    print(item)