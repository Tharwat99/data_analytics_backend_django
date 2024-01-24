from . models import Data
import django_filters

class DataListFilter(django_filters.FilterSet):
    """ 
    filter data using month, revenue, expenses, and profit
    """
    month = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Data
        fields = ["month", "revenue", "expenses", "profit"]
        order_by = ['-month', 'month','-revenue', 'revenue', '-expenses', 'expenses', '-profit', 'profit']