from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class HotelBanner(models.Model):
    image1 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image5 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image6 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)
    image7 = models.ImageField(upload_to='images/hotel_banner', blank=True, null=True)

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
    
    class Meta:
        verbose_name_plural = 'Menu Category'
    


class MenuList(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(MenuCategory, related_name='menucategory')
    price = models.FloatField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    


class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_image/')
    caption = models.CharField(max_length=1000)
    
    
class HotelData(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    hotel_phone = models.CharField(max_length=100)
    hotel_email = models.EmailField(max_length=100)
    hotel_website = models.URLField(max_length=100)
    hotel_description = models.TextField()
    hotel_image = models.ImageField(upload_to='hotel_image/')
    
    class Meta:
        verbose_name_plural = 'Hotel Data'
    
    def __str__(self):
        return self.hotel_name
    
class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_description = models.TextField()
    event_image = models.ImageField(upload_to='event_image/')
    
    class Meta:
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return self.event_name