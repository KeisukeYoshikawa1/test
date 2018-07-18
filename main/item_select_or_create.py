import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item

item, created = Item.objects.get_or_create(name='grape_juice', price=150)
print(item, '作成チェック：', created)