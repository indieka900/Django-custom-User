# Generated by Django 4.2.5 on 2023-09-21 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0008_alter_customuser_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
