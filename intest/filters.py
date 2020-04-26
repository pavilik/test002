import django_filters
from django_filters import FilterSet, ChoiceFilter

from intest.models import Person


class PersonFilter(FilterSet):
    endworkdate = django_filters.BooleanFilter(label='Работает ли',  field_name='endworkdate',
                                             lookup_expr='isnull')

    def filter_endworkdate(self, queryset, name, value):
        # construct the full lookup expression.
        #  lookup = '__'.join([name, 'None'])
        return queryset.filter(**{'endworkdate__isnull': False})

    class Meta:
        model = Person
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['endworkdate', 'department']
