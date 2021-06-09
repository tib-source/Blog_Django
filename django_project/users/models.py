from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # create a relationship with the user model 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(editable=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs): #extend the save module 
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
