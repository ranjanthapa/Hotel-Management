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


class RoomImage(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='room_image')
    image1 = models.ImageField(upload_to='images/room_image')
    image2 = models.ImageField(upload_to='images/room_image')
    image3 = models.ImageField(upload_to='images/room_image')
    image4 = models.ImageField(upload_to='images/room_image')
    image5 = models.ImageField(upload_to='images/room_image')

    def __str__(self):
        return f'Room Number: {self.room}'


class RoomDetail(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name='room_detail')
    image = models.ForeignKey(RoomImage, on_delete=models.PROTECT, null=True, blank=True)
    price = models.PositiveIntegerField()
    room_type = models.CharField(max_length=30, choices=ROOM_TYPE)
    bed_type = models.CharField(max_length=30, choices=BED_TYPE, blank=True, null=True)
    availability = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=ROOM_STATUS)
    amenities = models.TextField()


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Offers(models.Model):
    room = models.OneToOneField(RoomDetail, on_delete=models.CASCADE, related_name='room_offer')
    discount = models.PositiveIntegerField()
    offer_start = models.DateField()
    offer_end = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return f'Room Number: {self.room}'
#########################################################################################################
