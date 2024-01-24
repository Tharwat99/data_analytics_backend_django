from rest_framework import generics, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Data
from .serializers import DataListSerializer, DataUploadFileSerializer
from .filters import DataListFilter
from .utils import handle_csv_file


class DataListView(generics.ListAPIView):
    """
    DataListView for list all data.
    """
    queryset = Data.objects.all()
    serializer_class = DataListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = DataListFilter

class DataUploadFileView(generics.GenericAPIView):
    """
    DataUploadFileView for upload file data.
    """
    serializer_class = DataUploadFileSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_file = serializer.validated_data['data_file']
        try:
            data_list = handle_csv_file(data_file)
            Data.objects.bulk_create(data_list)
            return Response({'message': 'uploaded sucessfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Error: Error processing the file.'}, status=status.HTTP_400_BAD_REQUEST)
            