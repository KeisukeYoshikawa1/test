import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item

item, created = Item.objects.update_or_create(name='orange_juice', price=130, defaults={'price':140})
print(item, created)