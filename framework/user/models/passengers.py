from django.db import models


class Passengers(models.Model):
    id = models.AutoField(primary_key=True)
    booking = models.ForeignKey(
        'Bookings',
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(
        null=False, blank=False
    )
    gender_choices = (
        ('male', "Male"),
        ('female', 'Female'),
        ('others', 'Others')
    )
    gender = models.CharField(
        max_length=50,
        choices=gender_choices,
        null=True, blank=True,
        default="others"
    )

    class Meta:
        db_table = 'passengers'
        verbose_name_plural = "Passengers"
        verbose_name = "Passenger"

    def __str__(self):
        return self.first_name
