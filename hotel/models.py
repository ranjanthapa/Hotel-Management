from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


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
    