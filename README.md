# all_twitter_scraper
All twitter scraper gets all tweets filtered by the parameters that are in twitter advanced search such as tweets that: include specific keywords, does not include specific keywords, include exact phrase, include specific hashtags, etc..

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)

## Installation

To install all_twitter_scraper package, simply run:

```sh
pip install all_twitter_scraper
```

## Usage
An example that clears most of the package parameters:
```python
from all_twitter_scraper.Twitter_Scraper import Twitter_Scraper
from datetime import date
from all_twitter_scraper.Criteria import Criteria


if __name__ == "__main__":
	criteria = Criteria()
	criteria.set_language('ar')
	criteria.set_since_date(date(2019, 1, 1))
	criteria.set_until_date(date(2020, 4, 1))
	criteria.set_all_of_keywords(['Mohammed', 'Aly'])
	twitter_scraper = Twitter_Scraper()
	tweets = twitter_scraper.scrap(criteria, return_tweets_list=True)
```

## Buy me a coffee
<a href="https://www.paypal.me/abdallahaboelela" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>