from haystack import indexes
from webtagger.models import Sentence

class SentenceIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	sentence = indexes.CharField(model_attr='sentence')

	def get_model(self):
		return Sentence

	def index_queryset(self):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.all()