# Generated by Django 3.2.2 on 2022-10-21 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
