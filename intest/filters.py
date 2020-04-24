import django_filters
from django_filters import FilterSet

from intest.models import Person


class PersonFilter(FilterSet):

    endworkdate = django_filters.BooleanFilter(field_name='endworkdate', lookup_expr='isnull', exclude=True, method='filter_endworkdate',label='Работает ли')
    def filter_endworkdate(self, queryset, name, value):
        # construct the full lookup expression.
          #  lookup = '__'.join([name, 'None'])
            return queryset.filter(**{'endworkdate': None})

    class Meta:
        model = Person
        # Declare all your model fields by which you will filter
        # your queryset here:
        fields = ['endworkdate', 'department']

