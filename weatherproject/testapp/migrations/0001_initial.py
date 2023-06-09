# Generated by Django 4.2.1 on 2023-06-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('humidity', models.IntegerField()),
            ],
        ),
    ]
