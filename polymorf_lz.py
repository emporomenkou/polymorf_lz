import pandas as pd


class Dataframe:
    def __init__(self, filename: str):
        self.__df = pd.read_csv(filename, sep = ',')
    def grouping(self):
        a = self.__df.groupby('Результат операции') #группируем
        for type, group in a: #type - параметр, group - датафрейм имеющий этот параметр
            group.to_csv(f"результат-операции_{type}.csv", index = False) #заносим результат группировки в разные файлы
    def __neg__(self):
        print(f"Количество повторяющихся строк: {self.__df.duplicated().sum()}") #выводим кол-во дубликатов
        self.__df.drop_duplicates(inplace = True)

