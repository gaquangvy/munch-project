# Generated by Django 3.0.4 on 2020-05-05 01:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0021_auto_20200428_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='card_expdate',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='card_pin',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.Payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.Review'),
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.FloatField(default=5.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Customer'),
        ),
        migrations.AddField(
            model_name='payment',
            name='stripe_charge_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='header',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
