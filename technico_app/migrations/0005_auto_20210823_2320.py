# Generated by Django 3.2.3 on 2021-08-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technico_app', '0004_product_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cat',
            field=models.CharField(choices=[('1', 'hardware'), ('2', 'web dev'), ('3', 'AutomationTesting'), ('4', 'AI'), ('5', 'Hardware'), ('6', 'NewTechnology')], max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('1', 'hardware'), ('2', 'web dev'), ('3', 'AutomationTesting'), ('4', 'AI'), ('5', 'Hardware'), ('6', 'NewTechnology')], max_length=1),
        ),
    ]
