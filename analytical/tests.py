from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile

class DataListViewTests(APITestCase):
    def test_data_list_view(self):
        url = reverse('data-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DataUploadFileViewTests(APITestCase):
    url = reverse('data-upload-file')

    def test_valid_file_upload(self):
        # Create a sample CSV file in memory
        csv_content = "Month,Revenue,Expenses,Profit\nJan,100,50,50\nFeb,200,100,100"
        csv_file = SimpleUploadedFile("data.csv", csv_content.encode(), content_type="text/csv")
        # Send a POST request with the file
        response = self.client.post(self.url, {'data_file': csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_file_extension(self):
        # Create a sample non-CSV file in memory
        txt_file = SimpleUploadedFile("data.txt", b"Invalid file content.", content_type="text/plain")
        # Send a POST request with the non-CSV file
        response = self.client.post(self.url, {'data_file': txt_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['data_file'][0], "Only CSV files are supported.")

    def test_invalid_file_size(self):
        # Create a sample CSV file larger than the allowed size
        large_csv_content = "A" * (101 * 1024 * 1024)  # 101 MB
        large_csv_file = SimpleUploadedFile("large_data.csv", large_csv_content.encode(), content_type="text/csv")
        # Send a POST request with the large file
        response = self.client.post(self.url, {'data_file': large_csv_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['data_file'][0], "File size exceeds the allowed limit.")

    def test_missing_file(self):
        # Send a POST request without attaching a file
        response = self.client.post(self.url, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['data_file'][0], "No file was submitted.")
