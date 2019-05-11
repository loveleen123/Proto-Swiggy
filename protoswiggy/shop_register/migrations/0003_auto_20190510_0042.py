# Generated by Django 2.2 on 2019-05-09 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('shop_register', '0002_auto_20190501_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('shop_name', models.CharField(max_length=200)),
                ('shop_owner_name', models.CharField(max_length=200)),
                ('shop_address', models.TextField()),
                ('license_number', models.CharField(max_length=200)),
                ('shope_phone', models.CharField(max_length=200)),
                ('shop_gst', models.CharField(max_length=200)),
                ('application_date', models.DateTimeField(verbose_name='Application Date')),
                ('shop_license_pdf', models.FileField(upload_to='docs')),
                ('shop_owner_id_proof', models.FileField(upload_to='docs')),
                ('shop_owner_photo', models.FileField(upload_to='docs')),
                ('shop_approved', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='ShopApplications',
        ),
    ]
