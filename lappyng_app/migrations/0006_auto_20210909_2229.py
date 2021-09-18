# Generated by Django 3.2.7 on 2021-09-09 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lappyng_app', '0005_products_hot_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(blank=True, help_text='Use this Image dimension 170px X 100px', null=True, upload_to='uploads/', verbose_name='Category Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img_banner',
            field=models.ImageField(blank=True, help_text='Use this Image dimension 848px X 132px', null=True, upload_to='uploads/', verbose_name='Category Banner Image'),
        ),
    ]
