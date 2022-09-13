from django.db import models


class Bookings(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    flight = models.ForeignKey(
        'flights.Flights',
        on_delete=models.CASCADE,
        null=False, blank=False
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'bookings'
        verbose_name_plural = "Bookings"
        verbose_name = "Booking"

    def __str__(self):
        return self.flight.airline.name
