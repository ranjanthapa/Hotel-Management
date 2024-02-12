from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class HotelShortIntro(models.Model):
    introduction = models.TextField()
    video_url = models.URLField()

    class Meta:
        verbose_name = "Welcome Introduction"
        verbose_name_plural = "Welcome Introduction"

    def __str__(self):
        return f'Hotel Introduction'


class HotelContactInfo(models.Model):
    address = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    facebook_url = models.URLField(blank=True, null=True)
    x_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Hotel Information"

    class Meta:
        verbose_name = 'Hotel Contact Information'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile')
    statement = models.TextField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"Statement said by {self.name}"


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Food Category'


class MenuList(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(FoodCategory)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class BannerImage(models.Model):
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image2 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image3 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image4 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image5 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image6 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)
    image7 = models.ImageField(upload_to='hotel_banner', blank=True, null=True)


class History(models.Model):
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} in {self.year}"

    class Meta:
        verbose_name_plural = "History"
        ordering = ['-year']


class VisionAndGoal(models.Model):
    title = models.CharField(max_length=200)
    commitment = models.TextField()

    def __str__(self):
        return self.title



