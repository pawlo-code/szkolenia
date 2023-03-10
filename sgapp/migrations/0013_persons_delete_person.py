# Generated by Django 4.1.7 on 2023-02-17 17:02

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('sgapp', '0012_alter_person_aprrove'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', phone_field.models.PhoneField(help_text='Numer telefonu', max_length=31)),
                ('email', models.EmailField(max_length=50)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sgapp.training')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
