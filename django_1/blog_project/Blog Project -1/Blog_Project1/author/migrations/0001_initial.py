# Generated by Django 5.0 on 2023-12-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('bio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phoneNUmber', models.CharField(max_length=12)),
            ],
        ),
    ]
