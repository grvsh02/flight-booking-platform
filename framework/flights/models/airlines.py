from django.db import models


class Airlines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'airlines'
        verbose_name_plural = "Airlines"
        verbose_name = "Airline"

    def __str__(self):
        return self.name
