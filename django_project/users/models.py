from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # create a relationship with the user model 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(editable=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'
