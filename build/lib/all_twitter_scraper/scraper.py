from modules.Twitter_Scraper import Twitter_Scraper
from datetime import date
from modules.Criteria import Criteria


if __name__ == "__main__":
	criteria = Criteria()
	criteria.set_language('ar')
	criteria.set_since_date(date(2019, 1, 1))
	criteria.set_until_date(date(2019, 1, 16))
	criteria.set_all_of_keywords(['مرأة'])
	criteria.set_none_of_keywords([])
	twitter_scraper = Twitter_Scraper()
	twitter_scraper.scrap(criteria)
