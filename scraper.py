from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import time
from link_collector import LinkCollector
from item_data_collector import ItemDataCollector

SETTINGS_PATH = "settings.json"

class AutoruScraper:
    """ Main class for collect data & create data frame """

    def __init__(self, config_path: str = SETTINGS_PATH):
        # self.settings = ...
        # self.max_page = ... # Взять из settings
        # self.page_sleep_time = ...  # Взять из settings
        # self.item_sleep_time = ...  # Взять из settings
        # self.df_name = ...  # Взять из settings
        self.link_collector = LinkCollector()
        self.item_data_collector = ItemDataCollector()
    
    def get_current_df(self):
        try:
            df = pd.read_csv("./autoru_items.csv")
        except FileNotFoundError:
            return pd.DataFrame()
        return df
    
    def __call__(self):
        max_page = 3
        # print(settings)
        for i in range(0, max_page):
            new_urls = self.link_collector.grab_links(i)
            current_df = self.get_current_df()
            items = []
            for url in new_urls['item_link']:
                item = self.item_data_collector.scrape_page(url)
                if item != {}:
                    items.append(item)
                time.sleep(1)
            items_df = pd.DataFrame(items)
            new_current = pd.concat([current_df, items_df])
            new_current.to_csv("autoru_items.csv", index=False)
            print(f"Progress: {round((i+1) / max_page * 100, 2)}%")
            time.sleep(2)

if __name__ == "__main__":
    autoru_scraper = AutoruScraper()
    autoru_scraper()