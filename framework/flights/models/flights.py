from django.db import models


class Flights(models.Model):
    id = models.AutoField(primary_key=True)
    airline = models.ForeignKey(
        'Airlines',
        on_delete=models.CASCADE,
        blank=False, null=False
    )
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'flights'
        verbose_name_plural = "Flights"
        verbose_name = "Flight"

    def __str__(self):
        return self.flight_number
