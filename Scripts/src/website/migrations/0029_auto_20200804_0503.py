# Generated by Django 3.0.8 on 2020-08-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_auto_20200803_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='LabCode',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='LabName',
            field=models.CharField(max_length=60, null=True),
        ),
    ]