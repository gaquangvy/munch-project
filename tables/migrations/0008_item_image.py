# Generated by Django 3.0.4 on 2020-04-08 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20200406_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='/static/NoImageFound.jpg', upload_to='images/'),
        ),
    ]
