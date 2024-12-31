from django.contrib import admin
from django.urls import path

from ExcelApp.views import *

urlpatterns = [
    path('', ExcelExportImport.as_view()),
]