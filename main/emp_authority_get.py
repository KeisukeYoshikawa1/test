import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj.settings')
django.setup()

from item.models import Emp, Authority

emp = Emp.objects.get(id=1)
for authority in emp.authoritys.all():
    print(authority.name)

print()
authority = Authority.objects.get(id=1)
for emp in authority.emps.all():
    print(emp.name)