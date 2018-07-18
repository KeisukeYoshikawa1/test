import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Item
item = Item.objects.get(id=1)
del_count, del_item = item.delete()
print('削除件数：', del_count)