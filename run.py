from AutoScraper import Auto_Scraper
from Data_Cleaning import Data_Cleaning

if __name__ == '__main__':
    scrapper = Auto_Scraper(prompt="{prompt}")
    scrapper.start_search()
    data = scrapper.data_loop()
    scrapper.print_data()
    data = Data_Cleaning(scrapper.result_list , '{file_path}')
    data.Change_To_Csv()
