# Generated by Django 3.0.8 on 2020-07-28 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_auto_20200728_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docworkoncenter',
            name='CenterCode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='website.MedicalCenter'),
        ),
        migrations.AlterField(
            model_name='docworkoncenter',
            name='SynCode',
            field=models.CharField(max_length=30, null=True),
        ),
    ]