from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    @classmethod
    def get_image(cls,user):
        images = cls.objects.filter(user=user)
        return images


class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
