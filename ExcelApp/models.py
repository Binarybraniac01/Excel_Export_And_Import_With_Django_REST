from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    

class ExcelUpload(models.Model):
    uploadedfile = models.FileField(upload_to='imported_files') 


class NewStudent(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name