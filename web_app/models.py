from django.db import models  # type: ignore

TRANSMITTER_TYPES = [
    ("Передатчик", "Передатчик"),
    ("Приёмник", "Приёмник"),
    ("Приёмопередатчик", "Приёмопередатчик"),
]


# Create your models here.
class Satellite(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to="images/")
    status = models.CharField(max_length=200)
    is_frequency_violator = models.BooleanField()
    country = models.CharField(max_length=200)
    launch_date = models.DateField()

    def __str__(self):
        """
        Return a string representation of the Satellite model instance.

        Returns:
            str: The name of the satellite.
        """
        return self.name


class Transmitter(models.Model):
    id = models.AutoField(primary_key=True)
    satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TRANSMITTER_TYPES)
    status = models.CharField(max_length=200)
    upper_frequency_up = models.FloatField()
    lower_frequency_up = models.FloatField()
    upper_frequency_down = models.FloatField()
    lower_frequency_down = models.FloatField()
    modulation = models.CharField(max_length=200)
    is_inverted = models.BooleanField()
    baud_rate = models.FloatField()

    def __str__(self):
        """
        Return a string representation of the Transmitter model instance.

        Returns:
            str: The name of the transmitter.
        """
        return self.description


class Tle(models.Model):
    id = models.AutoField(primary_key=True)
    satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE)
    tle_0 = models.CharField(max_length=200)
    tle_1 = models.CharField(max_length=200)
    tle_2 = models.CharField(max_length=200)
    update_date = models.DateField()

    def __str__(self):
        """
        Return a string representation of the Tle model instance.

        Returns:
            str: The id of the TLE.
        """
        return str(self.id)

    class Meta:
        verbose_name = "TLE"
        verbose_name_plural = "TLEs"
        ordering = ["-update_date"]
