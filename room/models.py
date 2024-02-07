# from django.contrib.auth.models import User
from django.db import models
from account.models import Account
from phonenumber_field.modelfields import PhoneNumberField


class BaseRoomChoices(models.Model):
    class Meta:
        abstract = True

    _ROOM_TYPE = [
        ('single', 'Single'),
        ('family', 'Family'),
        ('deluxe', 'Deluxe'),
        ('president', 'President'),
    ]

    _ROOM_STATUS = [
        ('clean', 'Clean'),
        ('maintenance', 'Maintenance'),
        ('dirty', 'Dirty')
    ]

    _BED_TYPE = [
        ('single_bed', 'Single Bed'),
        ('double_bed', 'Double Bed'),
        ('king_bed', "King Bed")
    ]


class Room(BaseRoomChoices):
    room_no = models.PositiveIntegerField(unique=True)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.room_no)


class RoomImage(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/room_image')
    image2 = models.ImageField(upload_to='images/room_image')
    image3 = models.ImageField(upload_to='images/room_image')
    image4 = models.ImageField(upload_to='images/room_image')
    image5 = models.ImageField(upload_to='images/room_image')

    def __str__(self):
        return f'Room Number: {self.room}'


class RoomDetail(BaseRoomChoices):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='room_detail')
    image = models.ForeignKey(RoomImage, on_delete=models.PROTECT, null=True, blank=True)
    price = models.PositiveIntegerField()
    room_type = models.CharField(max_length=30, choices=BaseRoomChoices._ROOM_TYPE)
    bed_type = models.CharField(max_length=30, choices=BaseRoomChoices._BED_TYPE, blank=True, null=True)
    availability = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=BaseRoomChoices._ROOM_STATUS)
    amenities = models.TextField()
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Room {self.room} detail'


class Reservation(BaseRoomChoices):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    room_type = models.CharField(choices=BaseRoomChoices._ROOM_TYPE, max_length=30, blank=True)
    bed_type = models.CharField(choices=BaseRoomChoices._BED_TYPE, max_length=30, blank=True)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    check_in = models.DateField()
    check_out = models.DateField()
    message = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


#
# class Booking(models.Model):
#     reserved = models.

class BookingConfirmation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)

