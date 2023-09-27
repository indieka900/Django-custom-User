# Generated by Django 4.2.5 on 2023-09-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0012_alter_course_video_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video_length',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10, null=True),
        ),
    ]