from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    room_no = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.room_no)


ROOM_TYPE = [
    ('single', 'Single'),
    ('family', 'Family'),
    ('deluxe', 'Deluxe'),
    ('president', 'President'),
]

ROOM_STATUS = [
    ('clean', 'Clean'),
    ('maintenance', 'Maintenance'),
    ('dirty', 'Dirty')
]

BED_TYPE = [
    ('single_bed', 'Single Bed'),
    ('double_bed', 'Double Bed'),
    ('king_bed', "King Bed")
]


class RoomDetail(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    # room_image = models.ManyToManyField(RoomImage)
    price = models.PositiveIntegerField()
    room_type = models.CharField(max_length=30, choices=ROOM_TYPE)
    bed_type = models.CharField(max_length=30, choices=BED_TYPE,blank=True, null=True)
    availability = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=ROOM_STATUS)
    amenities = models.TextField()


class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
