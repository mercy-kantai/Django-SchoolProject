# Generated by Django 5.0.6 on 2024-06-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_duration', models.TimeField()),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('course_description', models.TextField()),
                ('course_id', models.PositiveSmallIntegerField()),
                ('course_teacher', models.CharField()),
                ('course_department', models.CharField()),
                ('course_syllabus', models.FileField(upload_to='')),
                ('course_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
            ],
        ),
    ]