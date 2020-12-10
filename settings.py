import json

class Settings:
    """ """

    def __init__(self, path: str):
        self.path = path

        with open(path, "r") as cfg:
            config: Dict = json.load(cfg)
        
        self.max_page = config['max_page']
        self.page_sleep_time = config['page_sleep_time']
        self.item_sleep_time = config['item_sleep_time']
        self.df_name = config['df_name']
        print("\tYour setting is:")
        print(f"max_page\t\t{self.max_page}")
        print(f"page_sleep_time\t\t{self.page_sleep_time}")
        print(f"item_sleep_time\t\t{self.item_sleep_time}")
        print(f"df_name\t\t{self.df_name}")