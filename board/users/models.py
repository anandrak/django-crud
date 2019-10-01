from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{ self.user.username } Profile'

    #this class has already have save method as a default but we're going to add some features
    #When overriding model's save method in Django, you should also pass *args and **kwargs to overridden method. 
    
    # commented because it cause an error with AWS S3 to solve it out check AWS lambda 

    
    # def save(self, *args, **kwargs):
    #     #first we need to inherit the former save method like this
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path) # I think this line of code is problem we need to get pics from S3 storage
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    