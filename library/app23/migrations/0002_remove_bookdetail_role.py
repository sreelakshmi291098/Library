# Generated by Django 3.2 on 2022-11-24 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app23', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdetail',
            name='role',
        ),
    ]
