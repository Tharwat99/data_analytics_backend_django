# Generated by Django 4.2.7 on 2024-01-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytical', '0003_alter_data_revenue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='revenue',
            field=models.IntegerField(),
        ),
    ]
