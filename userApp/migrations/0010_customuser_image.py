# Generated by Django 4.2.5 on 2023-09-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0009_alter_customuser_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
