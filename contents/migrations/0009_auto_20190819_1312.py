# Generated by Django 2.2.2 on 2019-08-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0008_focus_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='duration',
            field=models.CharField(max_length=30),
        ),
    ]
