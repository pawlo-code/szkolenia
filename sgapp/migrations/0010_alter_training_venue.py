# Generated by Django 4.1.7 on 2023-02-16 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0009_alter_training_training_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='venue',
            field=models.CharField(choices=[('Online', 'Online')], max_length=20),
        ),
    ]