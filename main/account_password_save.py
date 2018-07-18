import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Password, Account

password1 = Password(value='abcde')
password1.save()

account = Account(name='suzuki', password=password1)
account.save()