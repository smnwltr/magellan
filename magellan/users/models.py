from django.contrib.auth.models import AbstractUser
from django.db import models
from random import choice
from string import ascii_lowercase, digits
from uuid import uuid4


def id_generator(size=8, chars=ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size))


class CustomUser(AbstractUser):
    # add additional fields in here
    url_short = models.CharField(max_length=8, unique=True)
    home_town = models.CharField(max_length=50, null=True, blank=True)
    home_country = models.CharField(max_length=50, null=True, blank=True)
    handle = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.url_short:
            # Generate ID once, then check the db. If exists, keep trying.
            self.url_short = id_generator()
            while CustomUser.objects.filter(url_short=self.url_short).exists():
                self.url_short = id_generator()
        super(CustomUser, self).save()

    def __str__(self):
        return self.email


def get_image_filename(instance, filename):
    url_short = instance.user.url_short
    file_ending = filename.split('.')[-1]
    return 'users/profile_images/{}/{}.{}'.format(url_short, uuid4(), file_ending)


class ProfileImage(models.Model):
    user = models.ForeignKey(CustomUser, related_name='profile_images', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Profile_image')
