from django.urls import path
from .views import upload_csv, DataListView

urlpatterns = [
    path('list/', DataListView.as_view(), name='data-list'),
    path('upload-csv/', upload_csv, name='upload-data')
]
