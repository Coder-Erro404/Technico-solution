# Generated by Django 3.2.3 on 2021-08-20 13:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technico_app', '0002_alter_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.CharField(choices=[('1', 'Developer'), ('2', 'ManualTesting'), ('3', 'AutomationTesting'), ('4', 'AI'), ('5', 'HardwareComputer'), ('6', 'NewTechnology')], max_length=1)),
                ('product_name', models.CharField(max_length=500)),
                ('product_image', models.FileField(upload_to='add_images')),
                ('content', ckeditor.fields.RichTextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
