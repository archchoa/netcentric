from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
	url(r'^list_of_sentences/$', list_of_sentences, name='list_of_sentences'),
	url(r'^tag_word/$', tag_word, name='tag_word'),
	url(r'^upload_xml_file/$', upload_xml_file, name='upload_xml_file'),
	url(r'^upload_success/$', upload_success, name='upload_success'),
)
