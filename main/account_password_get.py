import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Account

account = Account.objects.get(id=1)
print(account.name, account.password.value)