import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Datasets:
    def __init__(self, filename: str):
        self.__df = pd.read_csv(filename, sep = ',')
    def getdata(self):
        a = self.__df.groupby('Результат операции')
        #return a
        print(a.get_group('неправильный ввод пин-кода'))
        print(self.__df.duplicated().sum())
        print(self.__df[self.__df.duplicated()])
dataset = Datasets('var8.csv')
dataset.getdata()