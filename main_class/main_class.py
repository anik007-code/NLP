import pandas as pd
from matplotlib import pyplot as plt

from configs.config_data import DATA


class Sentiment:
    def __init__(self):
        self.data = DATA
        self.main_data = []
        self.run()

    def run(self):
        self.print_data()

    def print_data(self):
        df = pd.read_csv(self.data)
        print(df)
