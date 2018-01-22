from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userprofileinfo(models.Model):
    user=models.OneToOneField(User)
    #additional fields
    portfolio_site=models.URLField(blank=True)
    #for profile pic user pillow library
    profile_pic=models.ImageField(upload_to="profile_pics",blank=True)


    def __str__(self):
        return self.user.username



