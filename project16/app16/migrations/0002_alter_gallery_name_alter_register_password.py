# Generated by Django 4.1.4 on 2023-03-09 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app16', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='register',
            name='Password',
            field=models.CharField(max_length=10),
        ),
    ]