# Generated by Django 3.2 on 2021-04-24 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20210424_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspecs',
            name='car_plan',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstApp.carplan'),
        ),
    ]
