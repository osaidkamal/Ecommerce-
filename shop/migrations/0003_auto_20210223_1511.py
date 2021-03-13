# Generated by Django 3.1.7 on 2021-02-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_customer_order_orderitem_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
