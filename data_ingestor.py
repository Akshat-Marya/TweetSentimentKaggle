import csv
import os
import re

class DataIngestor():

    def __init__(self, dir):
        # read
        self.data = self.read_csv(dir)
    
    def read_csv(self, dir):
        if not os.path.exists(dir):
            print("Wrong directory, file isnt here")
        else:
            with open(dir, 'r') as f:
                reader = csv.reader(f)
                for r in reader:
                    # clean text
                    r = self.data_cleaner(r)
                    print(r)
            
            return 1

    def data_cleaner(self, row):
        text = row[1]
        # change everything to small case
        text = text.lower()
        # TODO: Remove special characters; ex: @

        return text
            


if __name__=='__main__':
    di = DataIngestor(dir="assets/tweet-sentiment-extraction/train.csv")
    print()