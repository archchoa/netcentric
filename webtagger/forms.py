from django import forms
from models import Article, Sentence, SentenceTag, Word, WordFeature

#import re

class ArticleForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.tokenizer = kwargs.pop('tokenizer')
		super(ArticleForm, self).__init__(*args, **kwargs)
		
	class Meta:
		model = Article
		
	def save(self, force_insert=False, force_update=False, commit=True):
		article = super(ArticleForm, self).save(commit=False)
		sentences = self.tokenizer.tokenize(article.body.strip(), realign_boundaries=True)
		if commit:
			article.save()
			for key, sentence in enumerate(sentences):
				#words = re.findall(r'\w+', sentence, flags = re.UNICODE | re.LOCALE)
				sentence = SentenceForm(dict(article=article.id, sentence=sentence, sentence_number=key))
				s = sentence.save()
				#for word in words:
					#word = WordForm(dict(sentence=s.id, word=word))
					#word.save()
		return article
		
class SentenceForm(forms.ModelForm):
	class Meta:
		model = Sentence
		
class SentenceTagForm(forms.ModelForm):
	class Meta:
		model = SentenceTag
		
class WordForm(forms.ModelForm):
	class Meta:
		model = Word
		
class WordFeatureForm(forms.ModelForm):
	class Meta:
		model = WordFeature
		
class UploadXMLForm(forms.Form):
    file = forms.FileField()