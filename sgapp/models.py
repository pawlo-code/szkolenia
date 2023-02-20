from django.db import models
from phone_field import PhoneField

# Create your models here.

class Training(models.Model):
    trainings = (
        ('Szkolenie pomiarowe', 'Szkolenie pomiarowe'),
        ('Szkolenie G1/2/3', 'Szkolenie G1/2/3'),
    )
    venues = (
        ('Online', 'Online'),
    )

    training_date = models.DateField()
    venue = models.CharField(max_length=20, choices=venues)
    training_type = models.CharField(max_length=20, choices=trainings)
    training_price = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Szkolenia'

    def __str__(self):
        return f"Kurs: {self.training_type} Data: {self.training_date}"
    
class Persons(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneField(blank=False)
    email = models.EmailField(max_length=50)
    training = models.ForeignKey(Training, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = 'Ludziki'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







