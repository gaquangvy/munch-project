# Generated by Django 3.0.4 on 2020-04-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0013_auto_20200422_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
