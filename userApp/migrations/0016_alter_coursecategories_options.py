# Generated by Django 4.2.5 on 2023-09-27 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0015_coursecategories_rename_user_course_teacher_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecategories',
            options={'verbose_name': 'Course Category', 'verbose_name_plural': 'Course Categories'},
        ),
    ]