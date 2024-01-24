from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
import csv
from .models import Data
from .serializers import DataSerializer
from .filters import DataListFilter

@api_view(['POST'])
def upload_csv(request):
    csv_file = request.FILES['file']

    # Parse and store the CSV data
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row
    data_list = []
    for row in reader:
        data_list.append(
            {
                'month': row[0],
                'revenue': int(row[1]),
                'expenses': int(row[2]),
                'profit': int(row[3])
            }
        )
    Data.objects.bulk_create([Data(**data) for data in data_list])

    return Response({'message': 'File uploaded successfully.'})


class DataListView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DataListFilter