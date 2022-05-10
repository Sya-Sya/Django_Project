from django.db import models
from django.conf import settings
# Create your models here.

class RoomCat(models.Model):
    Category = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextFiled(max_length=2000, null=false)

    def __str__(self):
        return self.Category

class Room(models.Model):
    Room_number = models.IntegerField()
    Beds = models.IntegerField()
    Price = models.IntegerField()
    Description = models.TextField(max_length=2000, null=False)
    Image = models.ImageField(upload_to='room_image')
    Capacity = models.IntegerField()
    Category = models.ForeignKey(RoomCat, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Room no ={self.Room_number} Price = {self.Price} Beds = {self.Beds} Capacity = {self.Capacity} Category = {self.Category}'

class Booking(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Check_in = models.DateTimeField()
    Check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked From = {self.check_in.strftime("%d-%b-%Y %H:%M")} To = {self.check_out.strftime("%d-%b-%Y %H:%M")}{self.room}'

FLIGHT_CHOICE = (
    ('Local','Local'),
    ('International','International'),
    )

class FlightCat(models.Model):
    FlightType = models.CharField(max_length=50)
    Rate = models.FloatField()
    Description = models.TextField(max_length=2000)

    def __str__(self):
        return self.FlightType

class FlightType(models.Model):
    FlightCategory = models.ForeignKey(Flight,on_delete=models.CASCADE,null=True)
    People = models.IntegerFiled()
    Price = models.IntegerField()
    Description = models.TextField(max_length=2000, null=True)
    Image = models.ImageField(uplaod_to='photosUploadAdmin')
    FlightNumber = models.IntegerField()

    def __str__(self):
        return f'Flight number ={self.FlightNumber} Flight Category = {self.FlightCategory} Price = {self.Price} People = {self.People}'

class FlightBook(models.Model):
    User = models.ForeignKey(setting.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Flight = models.ForeignKey(FlightType, on_delete=models.CASCADE)
    Check_in = models.DateTimeField()
    Check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} booked Filght Type = {self.Flight} from = {self.}'