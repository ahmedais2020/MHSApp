# Generated by Django 3.0.8 on 2020-07-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200728_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]