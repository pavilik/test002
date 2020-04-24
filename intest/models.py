from django.db import models
from django.db.models import SET_NULL


class Person(models.Model):
    firstname = models.CharField(verbose_name='Имя', help_text="Тут должно быть Имя", max_length=30)
    surname = models.CharField(max_length=30)
    otch = models.CharField(max_length=30)
    borndate = models.DateField(blank=True, null=True)
    email = models.EmailField()
    phonenum = models.CharField(max_length=11)
    startworkdate = models.DateField(blank=True, null=True)
    endworkdate = models.DateField(blank=True, null=True)
    jobtitle = models.CharField(max_length=30)
    department = models.ForeignKey('Department', on_delete=SET_NULL, null=True,verbose_name='Подразделение')

    def __str__(self):
        # return f"{self.firstname, self.surname, self.otch, self.borndate, self.email, self.phonenum, self.startworkdate, self.endworkdate, self.jobtitle, self.department}"  # todo # return '%s, %s' % (self.last_name, self.first_name)
        return f"{self.surname, self.department}"

    class Meta:
        ordering = ["-surname"]


class Department(models.Model):
    departmentname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.departmentname}"




