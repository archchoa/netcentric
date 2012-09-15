import nltk
import string

# Tokenize text into words, punctuation, and whitespace tokens

class ModifiedWPTokenizer(nltk.tokenize.RegexpTokenizer):
    def __init__(self):
        nltk.tokenize.RegexpTokenizer.__init__(self, r'\w+|[^\w\s]|\s+')