# Generated by Django 3.0.8 on 2020-08-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_auto_20200803_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldata',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
