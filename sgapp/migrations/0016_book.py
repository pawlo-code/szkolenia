# Generated by Django 4.1.7 on 2023-02-19 08:40

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0015_alter_persons_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=50)),
                ('training', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sgapp.training')),
            ],
        ),
    ]
