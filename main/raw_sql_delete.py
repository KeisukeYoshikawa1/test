import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from django.db import connection
from item.models import Item

with connection.cursor() as C:
    C.execute('DELETE FROM item_item WHERE name = %s', ['coffee'])

for item in Item.objects.all():
    print(item)