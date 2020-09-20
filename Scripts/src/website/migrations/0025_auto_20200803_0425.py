# Generated by Django 3.0.8 on 2020-08-03 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_auto_20200803_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorperson',
            name='PerNationalId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='website.Citizen'),
        ),
        migrations.AlterField(
            model_name='personlab',
            name='PerNationalId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='website.Citizen'),
        ),
        migrations.AlterField(
            model_name='personmedicalcenter',
            name='PerNationalId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='website.Citizen'),
        ),
    ]