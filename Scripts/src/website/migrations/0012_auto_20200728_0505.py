# Generated by Django 3.0.8 on 2020-07-28 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200728_0247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratory',
            old_name='LabUserName',
            new_name='LabType',
        ),
    ]