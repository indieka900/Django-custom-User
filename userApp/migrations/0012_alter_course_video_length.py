# Generated by Django 4.2.5 on 2023-09-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0011_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video_length',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]