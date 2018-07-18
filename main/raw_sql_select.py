import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from django.db import connection
with connection.cursor() as C:
    C.execute('SELECT name FROM item_item WHERE price = %s', [140])
    rows = C.fetchall()
    print(rows)
