# Generated by Django 4.2.11 on 2024-04-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_code', models.CharField(max_length=10, unique=True)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_age', models.IntegerField()),
            ],
        ),
    ]
