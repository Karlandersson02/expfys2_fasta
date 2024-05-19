import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from astropy import modeling
import re

PATH = r'C:\Users\Junior\Documents\GitHub\expfys2_fasta\PerkinElmer\zoom_edge_resolution student 21.csv'

class Perkin:
    def __init__(self, path):
        self.data = {'x': [], 'y': []}
        with open(path, 'r') as file:
            wv_pattern = r'^\d+'
            tr_pattern = r'\d+,\d+$'
            for i, line in [pair for pair in enumerate(file) if pair[0]>=6]:
                wv = int(re.search(wv_pattern, line).group())
                tr = float(re.search(tr_pattern, line).group().replace(',', '.'))
                self.data['x'].append(wv)
                self.data['y'].append(tr)

    def table(self):
        print(pd.DataFrame.from_dict(self.data, orient='columns'))
    
    def __call__(self):
        plt.plot(self.data['x'], self.data['y'], color='black')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

Perkin21 = Perkin(PATH)
Perkin21()