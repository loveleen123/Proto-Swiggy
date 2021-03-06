# Generated by Django 2.2 on 2019-05-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mother_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_photo',
            field=models.FileField(blank=True, upload_to='pictures'),
        ),
    ]
