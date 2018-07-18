import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Category, Product

product1 = Product.objects.get(id=1)
print(product1.name, product1.category.name)

print()
category = Category.objects.get(id=1)
for product in category.products.all():
    print(product.name)