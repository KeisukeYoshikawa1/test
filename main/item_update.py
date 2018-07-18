import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
item = Item.objects.get(id=1)
item.price = 10000
item.save()