# Generated by Django 2.2 on 2019-05-11 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopadmin', '0008_auto_20190511_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]