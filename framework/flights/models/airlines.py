from django.db import models


class Airlines(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    # logo = models.ImageField(upload_to='airlines', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    slogan = models.CharField(max_length=100, null=True, blank=True)
    head_quaters = models.CharField(max_length=100, null=True, blank=True)
    established = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'airlines'
        verbose_name_plural = "Airlines"
        verbose_name = "Airline"

    def __str__(self):
        return self.name
