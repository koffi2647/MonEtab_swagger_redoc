# Generated by Django 5.1 on 2024-09-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Adress',
                'verbose_name_plural': 'Adress',
            },
        ),
    ]
