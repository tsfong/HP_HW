# Generated by Django 4.0 on 2021-12-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('animal', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=100)),
            ],
        ),
    ]
