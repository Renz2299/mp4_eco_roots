# Generated by Django 3.2.23 on 2024-01-15 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240115_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
