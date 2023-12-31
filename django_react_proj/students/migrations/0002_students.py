# Generated by Django 4.2.4 on 2023-08-16 13:44

from django.db import migrations


def create_data(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student(name="Joe Silver", email="joe@example.com",
            document="2234342", phone="0000000000").save()


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]
