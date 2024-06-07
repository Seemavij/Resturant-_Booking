from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

TIME_CHOICES = (
    ('08:00 AM', '08:00 AM'),
    ('09:00 AM', '09:00 AM'),
    ('10:00 AM', '10:00 AM'),
    ('11:00 AM', '11:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('13:00 PM', '13:00 PM'),
    ('14:00 PM', '14:00 PM'),
    ('15:00 PM', '15:00 PM'),
)




class Reservation(models.Model):

    """
    Creates model for table Booking
    """

    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    number_of_guests = models.IntegerField(default=1,
                                           validators=[MaxValueValidator(4),
                                                       MinValueValidator(1)])
    date = models.DateField()
    time = models.CharField(
        max_length=8, choices=TIME_CHOICES, default='08:00 AM',)

    def __str__(self):
        return self.name