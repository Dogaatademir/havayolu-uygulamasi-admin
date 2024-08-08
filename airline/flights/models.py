from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.city}, {self.country})"

class Airline(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name  

class Plane(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    registration_number = models.CharField(max_length=100)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return self.model




class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True, blank=True)  # Geçici olarak nullable yapıyoruz
   
    def __str__(self):
        return f"{self.flight_number}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"





