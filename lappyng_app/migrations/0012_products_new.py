# Generated by Django 3.2.7 on 2021-09-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0011_blogpost_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='new',
            field=models.BooleanField(default=1, verbose_name='New Arrivals'),
            preserve_default=False,
        ),
    ]
