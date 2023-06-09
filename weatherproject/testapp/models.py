from django.db import models

# Create your models here.


class Weather(models.Model):
    city = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()

    def __str__(self):
        return f"{self.city} - {self.condition} (Temperature: {self.temperature}°C, Humidity: {self.humidity}%)"
