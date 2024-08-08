from django.urls import path
from .views import *

urlpatterns = [
    path('', upload_file, name='index'),
    path('file_details/<uuid:file_id>/', file_details, name='file_details'),
    path('download_file/<uuid:unique_id>/', download_file, name='download_file'),
]