# Generated by Django 4.2.6 on 2023-10-10 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Image',
            field=models.FileField(upload_to='media'),
        ),
    ]
