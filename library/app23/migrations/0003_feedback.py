# Generated by Django 3.2 on 2022-11-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app23', '0002_remove_bookdetail_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('delay', models.IntegerField()),
                ('ammount', models.IntegerField()),
            ],
        ),
    ]
