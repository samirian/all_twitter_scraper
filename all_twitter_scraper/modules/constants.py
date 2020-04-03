
CHROME_WINDOWS_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
FIREFOX_WINDOWS_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/74.0'
INTERNET_EXPLORER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko'
CHROME_MAC_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

USER_AGENTS = [
	CHROME_MAC_USER_AGENT,
	CHROME_WINDOWS_USER_AGENT,
	FIREFOX_WINDOWS_USER_AGENT,
	INTERNET_EXPLORER_USER_AGENT
]

HEADERS = {
	'Host': "twitter.com",
	'User-Agent': '',
	'Accept': "application/json, text/javascript, */*; q=0.01",
	'Accept-Language': "en-US,en;q=0.5",
	'X-Requested-With': "XMLHttpRequest",
	'Referer': '',
	'Connection': "keep-alive"
}
