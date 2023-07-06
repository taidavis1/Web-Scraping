import time
import pandas as pd

class Data_Cleaning():
    def __init__(self , list , filepath):
        self.list = list
        self.filepath = filepath
    def Change_To_DataFrame(self):
        return pd.DataFrame.from_dict(self.list)
    def Change_To_Csv(self):
        print("Convert to CSV")
        self.Change_To_DataFrame().to_csv(self.filepath)
        time.sleep(1)
        print("Finish Convert")