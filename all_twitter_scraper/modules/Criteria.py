from datetime import date
import requests


class Criteria:
	def __init__(self):
		self.__all_of_keywords = []
		self.__search_query = ''
		self.__since_date = date(1, 1, 1)
		self.__until_date = date(1, 1, 1)
		self.__language = ''
		self.__exact_phrase = ''
		self.__any_of_keywords = []
		self.__none_of_keywords = []
		self.__hashtags = []
		self.__maximum_position = ''
	
	def load_from_dict(self, criteria: dict):
		pass

	def set_since_date(self, since_date: date):
		self.__since_date = since_date

	def set_until_date(self, until_date: date):
		self.__until_date = until_date

	def set_search_query(self, search_query: str):
		self.__search_query = search_query

	def set_language(self, language: str):
		self.__language = language

	def set_maximum_position(self, maximum_position: str):
		self.__maximum_position = maximum_position

	def set_exact_phrase(self, phrase: str):
		self.__exact_phrase = phrase

	def set_any_of_keywords(self, keywords: list):
		self.__any_of_keywords = keywords

	def set_all_of_keywords(self, keywords: list):
		self.__all_of_keywords = keywords

	def set_none_of_keywords(self, keywords: list):
		self.__none_of_keywords = keywords

	def set_hashtags(self, hashtags: list):
		self.__hashtags = hashtags

	def generate_search_url(self):
		search_query = ''
		if len(self.__search_query) > 0:
			search_query = search_query
		else:
			if len(self.__all_of_keywords) > 0:
				search_query += ' '.join(self.__all_of_keywords)
			if len(self.__exact_phrase) > 0:
				search_query += ' "' + self.__exact_phrase + '"'
			if len(self.__any_of_keywords) > 0:
				search_query += ' (' + ' OR '.join(self.__any_of_keywords) + ')'
			if len(self.__none_of_keywords) > 0:
				search_query += ' -' + ' -'.join(self.__none_of_keywords)
			if len(self.__hashtags) > 0:
				search_query += ' (' + ' OR '.join(self.__hashtags) + ')'
			search_query = requests.utils.quote(search_query)
		filter_token = ''
		if self.__until_date.year > 1:
			filter_token += ' until:' + self.__until_date.strftime('%Y-%m-%d')
		if self.__since_date.year > 1:
			filter_token += ' since:' + self.__since_date.strftime('%Y-%m-%d')
		if len(self.__language) > 0:
			filter_token += ' lang:' + self.__language
		'""'
		filter_token = requests.utils.quote(filter_token)
		search_url = 'https://twitter.com/i/search/timeline?f=tweets&vertical=news&q=' + search_query + filter_token + '&src=typd&&include_available_features=1&include_entities=1&max_position=' + self.__maximum_position + '&reset_error_state=false'
		return search_url

	def __str__(self):
		return 'all_of_keywords [' + ' '.join(self.__all_of_keywords) + ']' + ' any_of_keywords [' + ' '.join(self.__any_of_keywords) + '] none_of_keywords [' + ' '.join(self.__none_of_keywords) + '] hashtags [' + ' '.join(self.__hashtags) + '] exact phrase ' + self.__exact_phrase + ' language ' + self.__language + ' since ' + self.__since_date.strftime('%Y-%m-%d') + ' until ' + self.__until_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
	criteria = Criteria()
	# criteria.set_since_date(date(2019, 9, 9))
	# criteria.set_until_date(date(2020, 2, 2))
	criteria.set_all_of_keywords(['covid19', 'corona'])
	criteria.set_any_of_keywords(['covid19', 'corona'])
	criteria.set_none_of_keywords(['covid19', 'corona'])
	criteria.set_hashtags(['#covid19', '#corona'])
	criteria.set_exact_phrase('covid19 corona')
	print(criteria.generate_search_url())
	print(criteria)
