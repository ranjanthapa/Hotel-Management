from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


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

class Amenitie(models.Model):  
    name = models.CharField(max_length=100, blank=True) 

    def __str__(self):
        return self.name

class RoomImage(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='images/room_image')
    image2 = models.ImageField(upload_to='images/room_image')
    image3 = models.ImageField(upload_to='images/room_image')
    image4 = models.ImageField(upload_to='images/room_image')
    image5 = models.ImageField(upload_to='images/room_image')
    
    def get_images(self):
        return [self.image1, self.image2, self.image3, self.image4, self.image5]
    
    def __str__(self):
        return f'Room Number: {self.room}'


class RoomDetail(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    image = models.ForeignKey(RoomImage, on_delete=models.PROTECT, null=True, blank=True)
    price = models.PositiveIntegerField()
    room_type = models.CharField(max_length=30, choices=ROOM_TYPE)
    bed_type = models.CharField(max_length=30, choices=BED_TYPE, blank=True, null=True)
    availability = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=ROOM_STATUS)
    amenities = models.ManyToManyField(Amenitie, related_name='rooms')


class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)
    adults = models.PositiveIntegerField(default=1)
    children = models.PositiveIntegerField(default=0)
    check_in = models.DateField()
    check_out = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



#########################################################################################################

class ContactUs(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    
    phone_number_validator = RegexValidator(
        regex=r'^\d{10}$',  # 10 digits
        message='Phone number must be 10 digits long.',
        code='invalid_phone_number'
    )
    
    phone_number = models.IntegerField(validators=[phone_number_validator])
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = 'ContactUs'
    
    def __str__(self):
        return self.name
    
    
class Goal(models.Model):
    hotel_vision = models.CharField(max_length=100)
    mission = models.TextField()

class ReviewAndRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i,i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"
    
class AboutUs(models.Model):
    detail = models.TextField()
    goal = models.OneToOneField(Goal, on_delete=models.CASCADE)
    user_review = models.ForeignKey(ReviewAndRating, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'AboutUs'

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuList(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(MenuCategory)
    price = models.FloatField()
    description = models.TextField()
    

