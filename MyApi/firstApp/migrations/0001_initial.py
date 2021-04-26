# Generated by Django 3.2 on 2021-04-24 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=100)),
                ('production_year', models.CharField(max_length=10)),
                ('car_body', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=50)),
            ],
        ),
    ]