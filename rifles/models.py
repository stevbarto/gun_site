from django.db import models

class Rifle(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    caliber = models.CharField(max_length=50)
    action = models.CharField(max_length=50)

    weight_lbs = models.FloatField()
    barrel_length_in = models.FloatField()
    overall_length_in = models.FloatField(null=True, blank=True)

    twist_rate = models.CharField(max_length=20, blank=True)
    msrp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"