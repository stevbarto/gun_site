from django.db import models


class Caliber(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rifle(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='rifles'
    )

    model = models.CharField(max_length=100)

    action = models.ForeignKey(
        Action,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rifles'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('manufacturer', 'model')
        ordering = ['manufacturer', 'model']

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class RifleVariant(models.Model):
    rifle = models.ForeignKey(
        Rifle,
        on_delete=models.CASCADE,
        related_name='variants'
    )

    caliber = models.ForeignKey(
        Caliber,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='variants'
    )

    sku = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    weight_lbs = models.FloatField(null=True, blank=True)
    barrel_length_in = models.FloatField(null=True, blank=True)
    twist_rate = models.CharField(max_length=20, blank=True)
    overall_length_in = models.FloatField(null=True, blank=True)

    msrp = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('rifle', 'sku')
        ordering = ['rifle', 'caliber']

    def __str__(self):
        return f"{self.name} {self.sku}"