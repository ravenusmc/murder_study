
#This file will hold the class that will manipulate the data from data.csv file.

#Importing files that will be used for the project
import numpy as np
import pandas as pd

class Data():

    #This method will return the number of murders by the year that the user entered
    def by_year(self, year):
        self.__data = pd.read_csv('project/murder.csv', low_memory=False)
        count = len(self.__data[self.__data.Year == year])
        return count

    #This method will return the number of murders that occurred in the state
    #that the user entered.
    def by_state(self, state):
        self.__data = pd.read_csv('project/murder.csv', low_memory=False)
        count = len(self.__data[self.__data.State == state])
        return count
