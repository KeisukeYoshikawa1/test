import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
print(Item.objects.count())