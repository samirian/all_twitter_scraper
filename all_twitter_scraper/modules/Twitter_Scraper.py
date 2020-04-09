import requests
from lxml import etree
import json
from datetime import date
from .Criteria import Criteria
from .Tweet import Tweet
import time
import random
import csv
import os
from .constants import HEADERS
from .helpers import User_Agent_Rotator


class Twitter_Scraper:
	def __init__(self):
		self.__user_agent_rotator = User_Agent_Rotator()
		if not os.path.exists('log'):
			os.mkdir('log')
		self.__log_file = open(os.path.join('log', 'log.txt'), 'a', encoding='utf-8')

	def scrap(self, criteria: Criteria, last_maximum_position='', return_tweets_list=False):
		tweets = []
		counter = 0
		maximum_position = last_maximum_position
		output_file = open(str(criteria) + '.csv', 'w', encoding='utf-8', newline='')
		csv_writer = csv.DictWriter(output_file, ['Tweet body', 'Date', 'Likes', 'Retweets', 'Tweet link', 'Twitter link'])
		csv_writer.writeheader()
		output_file.flush()
		while True:
			criteria.set_maximum_position(maximum_position)
			search_url = criteria.generate_search_url()
			HEADERS['Referer'] = search_url
			json_response = self.get_json_response(search_url, HEADERS)
			self.__dump_json(json_response, os.path.join('log', 'last_response.json'))
			try:
				if json_response['new_latent_count'] <= 0:
					break
			except:
				break
			html_content = json_response["items_html"]
			dom = etree.HTML
			try:
				dom = etree.HTML(html_content)
			except:
				continue
			min_position = json_response["min_position"]
			self.__log('last min_position : ' + min_position + '\n')
			tweet_doms = dom.xpath('//li[contains(@class, "js-stream-item")]')
			new_tweets = []
			for tweet_dom in tweet_doms:
				tweet = Tweet(tweet_dom)
				new_tweets.append(tweet)
			if len(new_tweets) == 0:
				break
			for new_tweet in new_tweets:
				csv_writer.writerow({
					'Tweet body': new_tweet.get_tweet_text(),
					'Date': new_tweet.get_tweet_datetime().strftime('%I:%M %p - %d %b %Y'),
					'Likes': new_tweet.get_likes(),
					'Retweets': new_tweet.get_retweets(),
					'Tweet link': new_tweet.get_tweet_link(),
					'Twitter link': 'https://twitter.com/' + new_tweet.get_username()
				})
				output_file.flush()
			if return_tweets_list:
				tweets.extend(new_tweets)
			counter += len(new_tweets)
			print('                                                                                ', end='\r')
			print('Total scraped tweets :', counter, end='\r')
			time.sleep(2)
			maximum_position = min_position
		print('\n')
		return tweets
	
	def get_json_response(self, url: str, headers: dict):
		json_response = {}
		for trial in range(10):
			try:
				headers['User-Agent'] = self.__user_agent_rotator.get_user_agent()
				json_response = requests.get(url, headers=headers, timeout=15).json()
				break
			except Exception as e:
				print(e)
				if trial > 9:
					print('Can not fetch more tweets.')
					raise Exception
				else:
					time.sleep(5)
		return json_response

	def __log(self, string: str):
		self.__log_file.write(string)
		self.__log_file.flush()

	def __dump_json(self, json_dict: dict, filename: str):
		with open(filename, 'w', encoding='utf-8') as file:
			json.dump(json_dict, file, indent=4)

if __name__ == "__main__":
	criteria = Criteria()
	criteria.set_language('ar')
	criteria.set_since_date(date(2020, 3, 25))
	criteria.set_until_date(date(2020, 3, 26))
	criteria.set_search_keywords(['covid19'])
	twitter_scraper = Twitter_Scraper()
	twitter_scraper.scrap(criteria)
