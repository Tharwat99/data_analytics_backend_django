from django.urls import path
from .views import DataListView, DataUploadFileView

urlpatterns = [
    path('list/', DataListView.as_view(), name='data-list'),
    path('upload-file/', DataUploadFileView.as_view(), name='data-upload-file')
]
