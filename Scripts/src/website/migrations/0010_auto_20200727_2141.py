# Generated by Django 3.0.8 on 2020-07-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200727_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalcenter',
            name='CenterType',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
