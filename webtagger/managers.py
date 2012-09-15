from django.db import models

from django.db.models import Count

from app_settings import *

from random import randint

class SentenceQuerySet(models.query.QuerySet):
	def random(self):
		count = self.aggregate(count=Count('id'))['count']
		random_index = randint(0, count - 1)
		return self.all()[random_index]

class SentenceManager(models.Manager):
	def get_query_set(self):
		return SentenceQuerySet(self.model, using=self._db)
		
	def random(self):
		return self.get_query_set().random()

class SentenceTagQuerySet(models.query.QuerySet):
	def filter_by_role(self, role):
		return self.filter(user__role=role)

	def get_votes(self, tag):
		return self.filter(tag=tag)
		
	def get_filtered_votes(self, role, tag):
		return self.filter_by_role(role).get_votes(tag)
		
class SentenceTagManager(models.Manager):
	def get_query_set(self):
		return SentenceTagQuerySet(self.model, using=self._db)
	
	def filter_by_role(self, role):
		return self.get_query_set().filter_by_role(role)
	
	def get_votes(self, tag):
		return self.get_query_set().get_votes(tag)
		
	def get_positive_votes(self, role):
		return self.get_query_set().get_filtered_votes(role, POSITIVE)
		
	def get_neutral_votes(self, role):
		return self.get_query_set().get_filtered_votes(role, NEUTRAL)
		
	def get_negative_votes(self, role):
		return self.get_query_set().get_filtered_votes(role, NEGATIVE)
		
	def get_nao_votes(self, role):
		return self.get_query_set().get_filtered_votes(role, NOT_AN_OPINION)