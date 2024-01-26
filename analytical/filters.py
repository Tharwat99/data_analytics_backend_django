from . models import Data
import django_filters

class DataListFilter(django_filters.FilterSet):
    """ 
    filter data using month, revenue, expenses, and profit
    """
    month = django_filters.CharFilter(lookup_expr='icontains')
    revenue__gte = django_filters.NumberFilter(field_name='revenue', lookup_expr='gte')
    revenue__lte = django_filters.NumberFilter(field_name='revenue', lookup_expr='lte')
    expenses__gte = django_filters.NumberFilter(field_name='expenses', lookup_expr='gte')
    expenses__lte = django_filters.NumberFilter(field_name='expenses', lookup_expr='lte')
    profit__gte = django_filters.NumberFilter(field_name='profit', lookup_expr='gte')
    profit__lte = django_filters.NumberFilter(field_name='profit', lookup_expr='lte')
    
    class Meta:
        model = Data
        fields = ["month", "revenue__gte", "revenue__lte", "expenses__gte", "expenses__lte",
                "profit__gte", "profit__lte"]
        order_by = ['-month', 'month','-revenue', 'revenue', '-expenses', 'expenses', '-profit', 'profit']