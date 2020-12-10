from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from link_collector import LinkCollector
from item_data_collector import ItemDataCollector
from settings import Settings

SETTINGS_PATH = "settings.json"

class AutoruScraper:
    """ Main class for collect data & create data frame """

    def __init__(self, config_path: str = SETTINGS_PATH):
        self.settings = Settings(path=config_path)
        self.link_collector = LinkCollector()
        self.item_data_collector = ItemDataCollector()
    
    def get_current_df(self):
        try:
            df = pd.read_csv(self.settings.df_name)
        except FileNotFoundError:
            return pd.DataFrame()
        return df
    
    def __call__(self):
        for i in range(0, self.settings.max_page):
            new_urls = self.link_collector.grab_links(i)
            current_df = self.get_current_df()
            items = []
            for url in new_urls['item_link']:
                item = self.item_data_collector.scrape_page(url)
                if item != {}:
                    items.append(item)
                time.sleep(self.settings.item_sleep_time)
            items_df = pd.DataFrame(items)
            new_current = pd.concat([current_df, items_df])
            new_current.to_csv(self.settings.df_name, index=False)
            print(f"Progress: {round((i+1) / self.settings.max_page * 100, 2)}%")
            time.sleep(self.settings.page_sleep_time)

if __name__ == "__main__":
    autoru_scraper = AutoruScraper()
    autoru_scraper()