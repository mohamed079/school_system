# Generated by Django 4.1 on 2022-09-06 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='type',
            field=models.CharField(choices=[('trouser', 'Trouser'), ('T-shirt', 'T Shirt')], default='T-shirt', max_length=10),
        ),
    ]