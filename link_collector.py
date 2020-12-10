from bs4 import BeautifulSoup
import urllib.request

BASE_URL = "https://auto.ru/moskva/cars/all/"

class LinkCollector:
    """ Class for collecting link of announcement """

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def get_href(self, element):
        return element.get('href')

    def grab_links(self, page_number: int):
        page_url = self.base_url + f"?page={page_number}"
        page_content = urllib.request.urlopen(page_url)
        soup = BeautifulSoup(page_content, 'html.parser')
        items_element = soup.find_all('a', attrs={'class': 'ListingItemTitle-module__link'})
        items_urls = list(map(self.get_href, items_element))
        return items_urls
