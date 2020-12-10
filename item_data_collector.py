from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json

class ItemDataCollector:
    """ Class for collection data on the item page """

    def get_new_car_data(self, property_name, li_class):
        self.result[property_name] = self.soup.find('li', attrs={'class': li_class}) \
            .find('a', attrs={'class': 'CardInfoGrouped__cellValue'}).getText()

    def get_used_car_data_link_value(self, property_name, li_class):
        self.result[property_name] = self.soup.find('li', attrs={'class': li_class}) \
            .find('a', attrs={'class': 'Link_color_black'}).getText()

    def get_used_car_data_span_value(self, property_name, li_class):
        self.result[property_name] = self.soup.find('li', attrs={'class': li_class}) \
            .find_all('span', attrs={'class': 'CardInfoRow__cell'})[1].getText()

    def scrape_page(self, url: str):
        self.result = {}
        page_content = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(page_content, 'html.parser')

        # return empty dict if car sold
        if self.soup.find('div', attrs={'class': 'CardSold'}) != None:
            return self.result

        prefilled_data = json.loads(self.soup.find('div', attrs={'id': 'sale-data-attributes'}).get('data-bem'))['sale-data-attributes']

        self.result['km_age'] = prefilled_data['km-age']
        self.result['mark'] = prefilled_data['mark']
        self.result['model'] = prefilled_data['model']
        self.result['power'] = prefilled_data['power']
        self.result['segment'] = prefilled_data['segment']
        self.result['state'] = prefilled_data['state']
        self.result['transmission'] = prefilled_data['transmission']
        self.result['year'] = prefilled_data['year'] 
        self.result['engine-type'] = prefilled_data['engine-type'] 
        self.result['type'] = prefilled_data['type']

        self.result['region'] = self.soup.find('span', attrs={'class': 'MetroListPlace_nbsp'}).getText()

        if prefilled_data['state'] == "new":
            attributes_to_parse = [('color', 'CardInfoGrouped__row_color'), ('body_type', 'CardInfoGrouped__row_bodytype')]
            for attribute in attributes_to_parse:
                property_name, element_name = attribute
                self.get_new_car_data(property_name, element_name)
        else:
            attributes_to_parse = [
                ('body_type', 'CardInfoRow_bodytype', 'link'),
                ('color', 'CardInfoRow_color', 'link'),
                ('drive_type', 'CardInfoRow_drive', 'span'),
                ('wheell_type', 'CardInfoRow_wheel', 'span'),
                ('condition', 'CardInfoRow_state', 'span'),
                ('ownersCount', 'CardInfoRow_ownersCount', 'span'),
                ('is_customs', 'CardInfoRow_customs', 'span'),
            ]
            for attribute in attributes_to_parse:
                property_name, element_name, element_type = attribute
                if element_type == "link":
                    self.get_used_car_data_link_value(property_name, element_name)
                else:
                    self.get_used_car_data_span_value(property_name, element_name)

        self.result['price'] = prefilled_data['price']
        return self.result