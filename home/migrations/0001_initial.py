# Generated by Django 3.2.23 on 2024-01-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('contact_content', models.TextField()),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]