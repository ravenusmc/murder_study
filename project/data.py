
#This file will hold the class that will manipulate the data from data.csv file.

#Importing files that will be used for the project
import numpy as np
import pandas as pd

class Data():

    #This method will return the number of deaths by the year that the user entered
    def by_year(self, year):
        self.__data = pd.read_csv('project/murder.csv')
        murders_by_year = len(self.__data[self.__data.Year == year])
        # count = len(murders_by_year)
        # return count

data = Data()
year = 2011
count = data.by_year(year)
print(count)

# data = pd.read_csv('project/murder.csv')
# print(data.head())
