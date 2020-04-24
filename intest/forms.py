from django.forms import ModelForm

from intest.models import Department


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['departmentname']
