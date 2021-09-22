import csv
from random import random


class ReadCsvFile():

    def __init__(self,file):

        # user needs to pass the file path when the class is instantiated

        try:
            file = open(file)

        except FileNotFoundError:
            print("File not found")

        self.file = file

        self.reader = csv.DictReader(file)

    def read(self):
        return random.choice(self.reader)