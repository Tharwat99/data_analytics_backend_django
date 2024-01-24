from rest_framework import serializers
from .models import Data

class DataListSerializer(serializers.ModelSerializer):
    """
    DataListSerializer for return list of data.
    """
    class Meta:
        model = Data
        fields = ["month", "revenue", "expenses", "profit"]


class DataUploadFileSerializer(serializers.Serializer):
    """
    DataUploadFileSerializer for upload csv file and validate file extension and size.
    """

    data_file = serializers.FileField()
    MAX_FILE_SIZE_MB = 100

    def validate_data_file(self, value):
        # Check if the file has a valid extension and allowd size.
        valid_extensions = ['.csv']  # Add more extensions if needed
        if not any(value.name.lower().endswith(ext) for ext in valid_extensions):
            raise serializers.ValidationError("Only CSV files are supported.")
        if value.size > self.MAX_FILE_SIZE_MB * 1024 * 1024:
            raise serializers.ValidationError("File size exceeds the allowed limit.")
        return value
