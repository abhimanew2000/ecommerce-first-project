# Generated by Django 4.2.3 on 2023-08-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.FloatField(null=True),
        ),
    ]
