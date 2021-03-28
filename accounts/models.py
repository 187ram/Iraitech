from django.contrib.auth.models import User
#from cloudinary.models import CloudinaryField
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    # picture = CloudinaryField("avtaar",default='avtaar/default.jpg',
    #    folder = "avtaar/",
    #   # notification_url = "https://dashboard.heroku.com/apps/register-start/avatar",
    #    resource_type = "image",
    #    transformation=[
    #                    {'width': 150, 'height': 150, 'gravity': "center", 'crop': "thumb"},
    #                    ])

    def __str__(self):
        return f'{ self.user.username} Profile'
    