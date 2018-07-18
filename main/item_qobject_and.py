import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from django.db.models import Q
from item.models import Item

q1 = Q(price__gt=90) & Q(price__lt=130)
items = Item.objects.filter(q1)
for item in items:
    print(item)