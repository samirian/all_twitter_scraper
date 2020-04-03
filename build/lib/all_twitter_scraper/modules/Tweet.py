from lxml import etree
from datetime import datetime
from datetime import date


class Tweet:
	def __init__(self, tweet_dom: etree.HTML):
		self.__tweet_id = int
		self.__username = str
		self.__tweet_text = str
		self.__replies = int
		self.__retweets = int
		self.__likes = int
		self.__tweet_link = str
		self.__tweet_datetime = datetime
		self.__tweet_dom = tweet_dom
		self.__process_tweet_dom()
		# print('-----------------------------')
		# print(self.__tweet_id)
		# print(self.__username)
		# print(self.__tweet_text)
		# print(self.__replies)
		# print(self.__retweets)
		# print(self.__likes)
		# print(self.__tweet_link)
		# print(self.__tweet_datetime.strftime('%I:%M %p - %b %d, %Y'))
		# print('-----------------------------')

	def __process_tweet_dom(self):
			try:
				self.__tweet_id = self.__tweet_dom.xpath('.//div[contains(@class, "tweet")]')[0].get("data-tweet-id")
			except:
				self.__tweet_id = ''

			try:
				self.__username = self.__tweet_dom.xpath('.//div[@class="stream-item-header"]//span[contains(@class, "username")]')[0].xpath('string()').replace('@', '')
			except:
				self.__username = ''
			
			try:
				self.__tweet_text = self.__tweet_dom.xpath('.//p[contains(@class, "tweet-text")]')[0].xpath('string()')
			except:
				self.__tweet_text = ''

			try:
				self.__replies = int(self.__tweet_dom.xpath('.//span[contains(@class, "reply")]/span[@class="ProfileTweet-actionCount"]')[0].get("data-tweet-stat-count").replace(",", ""))
			except:
				self.__replies = 0

			try:
				self.__retweets = int(self.__tweet_dom.xpath('.//span[contains(@class, "retweet")]/span[@class="ProfileTweet-actionCount"]')[0].get("data-tweet-stat-count").replace(",", ""))
			except:
				self.__retweets = 0

			try:
				self.__likes = int(self.__tweet_dom.xpath('.//span[contains(@class, "favorite")]/span[@class="ProfileTweet-actionCount"]')[0].get("data-tweet-stat-count").replace(",", ""))
			except:
				self.__likes = 0

			try:
				self.__tweet_link = 'https://twitter.com' + self.__tweet_dom.xpath('.//div[contains(@class, "tweet")]')[0].get("data-permalink-path")
			except:
				self.__tweet_link = ''
				
			# tweet.author_id = int(tweetPQ("a.js-user-profile-link").attr("data-user-id"))
			try:
				datetime_string = self.__tweet_dom.xpath('.//small[@class="time"]/a')[0].get("title")
				self.__tweet_datetime = datetime.strptime(datetime_string, '%I:%M %p - %d %b %Y')
			except:
				self.__tweet_datetime = date(1, 1, 1)

			# tweet.hashtags, tweet.mentions = TweetManager.getHashtagsAndMentions(tweetPQ)

			# geoSpan = tweetPQ('span.Tweet-geo')
			# if len(geoSpan) > 0:
			# 	tweet.geo = geoSpan.attr('title')
			# else:
			# 	tweet.geo = ''

			# urls = []
			# for link in tweetPQ("a"):
			# 	try:
			# 		urls.append((link.attrib["data-expanded-url"]))
			# 	except KeyError:
			# 		pass

			# tweet.urls = ",".join(urls)

	def get_tweet_id(self):
		return self.__tweet_id

	def get_username(self):
		return self.__username

	def get_tweet_text(self):
		return self.__tweet_text

	def get_replies(self):
		return self.__replies

	def get_retweets(self):
		return self.__retweets

	def get_likes(self):
		return self.__likes

	def get_tweet_link(self):
		return self.__tweet_link

	def get_tweet_datetime(self):
		return self.__tweet_datetime
