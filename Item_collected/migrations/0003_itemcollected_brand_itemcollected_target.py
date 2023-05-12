# Generated by Django 4.1.7 on 2023-05-12 05:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand_product', '0001_initial'),
        ('Item_collected', '0002_alter_itemcollected_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcollected',
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='brand_product.brand_product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemcollected',
            name='target',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
