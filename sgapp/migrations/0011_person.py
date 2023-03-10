# Generated by Django 4.1.7 on 2023-02-17 16:33

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0010_alter_training_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Numer telefonu', max_length=31)),
                ('email', models.EmailField(max_length=50)),
                ('aprrove', models.BooleanField(default=False)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgapp.training')),
            ],
        ),
    ]
