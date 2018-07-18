import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
items = Item.objects.all()

for item in items:
    print(item)


# カラム指定
item_names = Item.objects.all().values('name')
for item_name in item_names:
    print(item_name)