from haystack.utils import Highlighter

class BorkHighlighter(Highlighter):
	def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
		highlighted_chunk = self.text_block[start_offset:end_offset]

		for word in self.query_words:
			highlighted_chunk = highlighted_chunk.replace(word, 'Bork!')

		return highlighted_chunk
		
class BoldHighlighter(Highlighter):
	def render_html(self, highlight_locations=None, start_offset=None, end_offset=None):
		highlighted_chunk = self.text_block[start_offset:end_offset]
	
		for word in self.query_words:
			highlighted_chunk = highlighted_chunk.lower().replace(word, '<span class="label label-warning">%s</span>' % word)

		return highlighted_chunk