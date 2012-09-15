from django.db import models

from accounts.models import UserProfile

from app_settings import *
from managers import *

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100, blank=True, null=True)
	date = models.DateField()
	body = models.TextField()
	link = models.URLField()
	
	def __unicode__(self):
		return self.title

class Sentence(models.Model):
	article = models.ForeignKey('Article')
	sentence = models.TextField()
	sentence_number  = models.IntegerField()
	
	objects = SentenceManager()
	
	def __unicode__(self):
		return self.sentence
		
class SentenceTag(models.Model):
	sentence = models.ForeignKey('Sentence')
	tag = models.IntegerField()
	user = models.ForeignKey(UserProfile)
	
	objects = SentenceTagManager()
	
	def tag_name(self):
		if self.tag == POSITIVE:
			return 'Positive'
		elif self.tag == NEUTRAL:
			return 'Neutral'
		elif self.tag == NEGATIVE:
			return 'Negative'
		elif self.tag == NOT_AN_OPINION:
			return 'Not an Opinion'
			
class Word(models.Model):
	word = models.CharField(max_length=100)
	sentence = models.ForeignKey('Sentence')
	
	def __unicode__(self):
		return self.word
		
class Feature(models.Model):
	name = models.CharField(max_length=45)
	tag = models.CharField(max_length=45)
	
	def __unicode__(self):
		return self.name

class WordFeature(models.Model):
	word = models.ForeignKey('Word')
	feature = models.ForeignKey('Feature')