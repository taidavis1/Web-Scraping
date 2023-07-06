from AutoScraper import Auto_Scraper
from Data_Cleaning import Data_Cleaning

if __name__ == '__main__':
    scrapper = Auto_Scraper(prompt="nails salon in Merced")
    scrapper.start_search()
    index = 1
    jump = 20
    data = scrapper.data_loop(index , jump)
    scrapper.print_data()
    data = Data_Cleaning(scrapper.result_list , 'C:/Users/V3 DESKTOP 3/Desktop/All Proejcts/Python learning/Web_Scraping/csv_files/data.csv')
    data.Change_To_Csv()