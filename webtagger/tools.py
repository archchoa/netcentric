import datetime
import nltk.data

from lxml import etree
from forms import ArticleForm
from time import strptime

def parse_xml_file(file):
	context = etree.iterparse(file)
	article_dict = {}
	date_dict = {}
	articles = []
	
	tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	
	for action, elem in context:
		if not elem.text:
			text = "None"
		else:
			text = elem.text
		if elem.tag == "article":
			articles.append(article_dict)
			article = ArticleForm(article_dict, tokenizer=tokenizer)
			article.save()
			article_dict = {}
		elif elem.tag == "day" or elem.tag == "month" or elem.tag == "year":
			date_dict[elem.tag] = text
		elif elem.tag == "date":
			month_name = date_dict['month']
			month_number = strptime(month_name, '%B').tm_mon
			date = datetime.date(int(date_dict['year']), month_number, int(date_dict['day']))
			article_dict["date"] = date
			date_dict = {}
		else:
			article_dict[elem.tag] = text