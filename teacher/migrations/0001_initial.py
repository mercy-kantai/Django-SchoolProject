# Generated by Django 5.0.6 on 2024-06-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code_id', models.PositiveSmallIntegerField()),
                ('country', models.CharField()),
                ('course_taught', models.CharField()),
                ('class_taught', models.CharField()),
                ('phone_number', models.CharField()),
                ('department', models.CharField()),
                ('office_hours', models.CharField()),
            ],
        ),
    ]
