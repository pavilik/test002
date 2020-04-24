import django.contrib
from intest.models import Person, Department

django.contrib.admin.site.register(Person)
django.contrib.admin.site.register(Department)
# Register your models here.
