import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
del_count, del_item = Item.objects.filter(name='coke').delete()
print('削除件数：', del_count)
