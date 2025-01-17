# Generated by Django 5.1.4 on 2024-12-31 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedfile', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.CreateModel(
            name='NewStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
