from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import * 
from .serializer import *

import pandas as pd
import uuid
from django.conf import settings


class ExcelExportImport(APIView):

    #TODO: run ExcelApp\faker.py files function first to populate the database 

    # Below will export the the current data in database to excel
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        df = pd.DataFrame(serializer.data)
        # print(df)

        df.to_csv(f"public/media/exported_files/{uuid.uuid4()}.csv", encoding="UTF-8", index=False)

        return Response({ "status": 200})


    # This will import from csv file and upload the data to database
    def post(self, request):
        excel_upload_obj = ExcelUpload.objects.create(uploadedfile = request.FILES['files'])
        df = pd.read_csv(f"{settings.BASE_DIR}/public/media/{excel_upload_obj.uploadedfile}") # needs absolute path

        for i in df.values.tolist(): # df.values.tolist() is used to view the csv data
            # print(i)
            NewStudent.objects.create(    # Uploaded values to the database 
                name = i[1],
                father_name = i[2],
                address = i[3],
                age = i[4]
            )

        return Response({ "status" : 200 })
