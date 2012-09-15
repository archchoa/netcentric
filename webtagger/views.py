from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe

from app_settings import *
from forms import UploadXMLForm, SentenceTagForm, WordForm
from models import Article, Sentence, SentenceTag, Word
from tools import parse_xml_file

import re

@staff_member_required
def upload_xml_file(request):
	if request.method == 'POST':
		form = UploadXMLForm(request.POST, request.FILES)
		if form.is_valid():
			parse_xml_file(request.FILES['file'])
			return HttpResponseRedirect(reverse('upload_success'))
	else:
		form = UploadXMLForm()
	return render_to_response('webtagger/upload_xml_file.html', {
		'form': form,
	}, context_instance=RequestContext(request))

@staff_member_required
def upload_success(request):
	return render_to_response('webtagger/upload_success.html', {

	}, context_instance=RequestContext(request))

@login_required	
def list_of_sentences(request):
	profile = request.user.get_profile()
	
	sentence_obj = Sentence.objects.random()
	
	words = re.findall(r'\w+', sentence_obj.sentence, flags = re.UNICODE | re.LOCALE)
	
	for word in words:
		sentence_obj.sentence = mark_safe(re.sub(r'\b%s\b' % word, "<span class='highlight'>%s</span>" % word, sentence_obj.sentence))
	
	if request.method == 'POST':
		if 'sentence_id' in request.POST:
			sentence_id = request.POST['sentence_id']
			if 'positive' in request.POST:
				tag = 'Positive'
				form = SentenceTagForm({'tag': POSITIVE, 'sentence': sentence_id, 'user': profile.id})
				form.save()
			elif 'neutral' in request.POST:
				tag = 'Neutral'
				form = SentenceTagForm({'tag': NEUTRAL, 'sentence': sentence_id, 'user': profile.id})
				form.save()
			elif 'negative' in request.POST:
				tag = 'Negative'
				form = SentenceTagForm({'tag': NEGATIVE, 'sentence': sentence_id, 'user': profile.id})
				form.save()
			elif 'noa' in request.POST:
				tag = 'Not an Opinion'
				form = SentenceTagForm({'tag': NOT_AN_OPINION, 'sentence': sentence_id, 'user': profile.id})
				form.save()
			else:
				tag = None
		else:
			tag = None
	else:
		tag = None
	
	return render_to_response('webtagger/list_of_sentences.html', {
		'sentence_obj': sentence_obj,
		'words': words,
		'tag': tag,
	}, context_instance=RequestContext(request))
	
@login_required
def tag_word(request):
	if request.method == 'POST':
		if 'word' in request.POST and 'sentence_id' in request.POST and 'feature_id' in request.POST:
			word = request.POST['word']
			sentence_id = int(request.POST['sentence_id'])
			feature_id = int(request.POST['feature_id'])
			
			#sentence = Sentence.objects.get(pk=sentence_id)
			#word = Word.objects.get_or_create(word=word, sentence=sentence)
		
			return HttpResponse(status=200)
		return HttpResponse(status=500)
	return HttpResponse(status=500)