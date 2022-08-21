from weakref import proxy
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
import requests
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from views import ForgotPasswordReset
# from home import views

# Create your models here.
class UserData(models.Model):
    user_id = models.CharField(max_length=255)
    user_pass = models.TextField()
    is_active = models.BooleanField(default=False)
    # personal details
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    def __str__(self):
        return '%s' % (self.user_id)
    
class ResetToken(models.Model):
    user_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    hash_pass = models.TextField(default='')
    def __str__(self):
        return '%s' % (self.user_id)




class TestModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
 
    def __str__(self):
        return self.title


    # print(response.json())


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)


class UpperCase(Profile):
    print('WE are hree..')
    class Meta:
        proxy = True
        def __str__(self):
           
            return self.city.upper()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()