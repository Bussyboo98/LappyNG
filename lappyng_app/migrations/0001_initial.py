# Generated by Django 3.2.7 on 2021-09-09 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abt_content', tinymce.models.HTMLField(verbose_name='Content')),
                ('image', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('image1', models.FileField(blank=True, upload_to='uploads/')),
                ('image2', models.FileField(blank=True, upload_to='uploads/')),
                ('image3', models.FileField(blank=True, upload_to='uploads/')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='This will automatically add a time when you click save')),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '4. About',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pst_title', models.CharField(max_length=150, verbose_name='Post Title')),
                ('slug', models.SlugField(unique=True)),
                ('pst_image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Post Image')),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('appear_home', models.CharField(choices=[('Feature', 'Appear on home'), ('No Feature', "Don't show on home"), ('', 'Please Choose')], default='', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Posted By')),
            ],
            options={
                'verbose_name_plural': '5. Blog Post',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=30, unique=True, verbose_name='Brand')),
                ('slug', models.SlugField(unique=True)),
                ('brand_img', models.ImageField(blank=True, help_text='Use this Image dimension 157px X 88px', null=True, upload_to='', verbose_name='Brand Image')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '2. Brand',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100, unique=True, verbose_name='Category')),
                ('slug', models.SlugField(unique=True)),
                ('cat_img', models.ImageField(blank=True, help_text='Use this Image dimension 170px X 100px', null=True, upload_to='', verbose_name='Category Image')),
                ('cat_img_banner', models.ImageField(blank=True, help_text='Use this Image dimension 848px X 132px', null=True, upload_to='', verbose_name='Category Banner Image')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lappyng_app.category')),
            ],
            options={
                'verbose_name_plural': '1. Category',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='New Price')),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Old Price')),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('contents', tinymce.models.HTMLField(verbose_name='Content')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('new_product', models.BooleanField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='lappyng_app.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='lappyng_app.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. Products',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lappyng_app.blogpost')),
            ],
            options={
                'verbose_name_plural': '6. Comments',
            },
        ),
    ]
