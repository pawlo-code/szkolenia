# Generated by Django 4.1.7 on 2023-02-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0006_alter_training_training_type_alter_training_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='training_type',
            field=models.CharField(choices=[('S', 'Szkolenie pomiarowe'), ('s2', 'Szkolenie G1/2/3')], max_length=2),
        ),
        migrations.AlterField(
            model_name='training',
            name='venue',
            field=models.CharField(choices=[('Inne...', 'Inne...')], max_length=20),
        ),
    ]
