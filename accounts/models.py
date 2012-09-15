from django.contrib.auth.models import User
from django.db import models
	
class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	role = models.IntegerField()
	
	def __unicode__(self):
		return self.user.username