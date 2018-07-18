import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Category, Product

category1 = Category(name='stationery')
category1.save()

product1 = Product(name='pencil', category=category1)
product1.save()

product2 = Product(name='note', category = category1)
product2.save()
