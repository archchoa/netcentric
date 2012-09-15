from django.contrib.auth.models import User
from django.db.models.signals import post_save

from app_settings import *
from models import UserProfile

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.get_or_create(user=instance, role=EXPERT) # for the time being...

post_save.connect(create_user_profile, sender=User)