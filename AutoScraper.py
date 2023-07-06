import os
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchAttributeException , NoSuchElementException
from selenium import webdriver

class Auto_Scraper():
    def __init__(self, prompt):
        self.driver = webdriver.Chrome()
        self.result_list = []
        self.prompt = prompt
        self.url = ""
    def start_search(self):
        self.driver.get("https://www.google.com/")
        element = self.driver.find_element(By.XPATH , '//*[@id="APjFqb"]')
        element.send_keys(self.prompt)
        element.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH , '//*[@id="Odp5De"]/div/div/div[1]/div[2]/div[1]/div[2]/g-more-link/a/div').click()
        time.sleep(1)
        self.url = self.driver.current_url
        print("Search Completed! ")
        time.sleep(2)
    def check_phone_nums(self , index):                      
        try:                                                   
            phone_nums = self.driver.find_element(By.XPATH , f'//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{index}]/div[1]/div/div/div/div[2]/div[3]/span[3]')
            return phone_nums.text
        except NoSuchElementException:            
            return "False"                        
    def check_data(self , index):                 
        try: 
            time.sleep(1)                          
            self.driver.find_element(By.XPATH , f'//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{index}]/div[2]/div/div/div/div/div/div[1]/a/div/div/button/span[2]')
            return True
        except NoSuchElementException:
            try:
                title = self.driver.find_element(By.XPATH , f'//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{index}]/div[1]/div/div/div/div[2]/div[1]/div')
                phone_number = self.check_phone_nums(index=index)
                if phone_number != "False":
                    data = {                                      
                        "Name " : title.text,
                        "Phone Number ": phone_number
                    }
                    self.result_list.append(data)
                    return True
                else:
                    self.result_list.append({
                        "Name ": title.text,
                        "Phone Number ": ' ' 
                    })
                    return True
            except NoSuchElementException:
                return False
    def check_btn(self):
        try: 
            self.driver.find_element(By.XPATH , '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[2]/div/div/button')
            return True
        except NoSuchElementException:
            return False
    def data_loop(self , index , jump):
        while index:
            case = self.check_data(index)
            if not case:
                index = 1
                self.driver.get(self.url + "&lci=" + str(jump))
                time.sleep(1)
                if not self.check_btn():
                    print("Loop Complete Done !")
                    self.driver.close()
                    self.driver.quit()
                    break
                jump += 20
                continue
            index += 2
    def print_data(self):
        for i in self.result_list:
            print(i)