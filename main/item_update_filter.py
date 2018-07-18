import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
up_count = Item.objects.filter(name='coke').update(price=9999)
print('更新件数:' , up_count)