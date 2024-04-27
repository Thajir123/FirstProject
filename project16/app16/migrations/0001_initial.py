# Generated by Django 4.1.6 on 2023-03-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Brand', models.CharField(max_length=10)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Age', models.IntegerField()),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('Place', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
    ]