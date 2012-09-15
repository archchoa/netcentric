from django.contrib import admin
from models import Article, Feature, Sentence, SentenceTag, Word, WordFeature

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date', 'body', 'link',)
	search_fields = ['title', 'author', 'date', 'body', 'link',]
	
admin.site.register(Article, ArticleAdmin)

class SentenceAdmin(admin.ModelAdmin):
	list_display = ('article', 'sentence', 'sentence_number',)
	search_fields = ['article', 'sentence', 'sentence_number',]
	
admin.site.register(Sentence, SentenceAdmin)

class SentenceTagAdmin(admin.ModelAdmin):
	list_display = ('user', 'tag_name', 'sentence',)
	search_fields = ['user', 'tag', 'sentence',]
	
admin.site.register(SentenceTag, SentenceTagAdmin)

class WordAdmin(admin.ModelAdmin):
	list_display = ('word','sentence',)
	search_fields = ['word','sentence',]
	
admin.site.register(Word, WordAdmin)

class FeatureAdmin(admin.ModelAdmin):
	list_display = ('name','tag',)
	search_fields = ['name','tag',]
	
admin.site.register(Feature, FeatureAdmin)

class WordFeatureAdmin(admin.ModelAdmin):
	list_display = ('word','feature',)
	search_fields = ['word','feature',]
	
admin.site.register(WordFeature, WordFeatureAdmin)