# Generated by Django 4.2.7 on 2024-01-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytical', '0004_alter_data_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='revenue',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
