import django_filters
from django_filters import DateFilter, DateFromToRangeFilter

from .models import Vehicleexpense,Dailyexpense



class VehicleexpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', input_formats=['%d%b%y'])
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', input_formats=['%d%b%y'])

    class Meta:
        model = Vehicleexpense
        fields = '__all__'
        exclude = ['vehicle','category','note','price', 'customer', 'mileage', 'description', 'date_updated','date_created']


class DailyexpenseFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', input_formats=['%d%b%y'])
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', input_formats=['%d%b%y'])

    class Meta:
        model = Dailyexpense
        fields = ['name']

