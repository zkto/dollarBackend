# Generated by Django 2.2.1 on 2019-06-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DollarClp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date', models.DateField(unique=True)),
                ('price_difference', models.FloatField()),
                ('date_update', models.DateTimeField(blank=True, null=True)),
                ('business_day', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dollar_clp',
            },
        ),
    ]