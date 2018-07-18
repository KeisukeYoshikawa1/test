import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Authority, Emp

authority1 = Authority(name='read')
authority1.save()

authority2 = Authority(name='regist')
authority2.save()

emp1 = Emp(name='satou')
emp1.save()

emp1.authoritys.add(authority1)
emp1.authoritys.add(authority2)

emp2 = Emp(name='suzuki')
emp2.save()

emp2.authoritys.add(authority1)