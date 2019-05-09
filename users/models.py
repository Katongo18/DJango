from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='11.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
# Create your models here.

    def save(self):
        super().save()  # save image from the super class(Profile)

        img = Image.open(self.image.path)  # open the image which is in the current path

        if img.height > 300 or img.width > 300:
            output_size = (200, 200)  # resizes the image to 300 * 300 if line 20 is met
            img.thumbnail(output_size)  # changes the img thumbnail with the desired size (in this case 300*300)
            img.save(self.image.path)  # saves the image and overides the current one
        
