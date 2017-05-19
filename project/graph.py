#This file will hold the class that will manipulate the data from murder.csv file.
#It will not actually run in the program but provide me with the code to make the
#graph images which I will insert into the program. I also used the entire
#CSV file to make my images. Thus, the data goes from 1980-2014. I include this
#file only to show others how I made the graphs and for my own personal records.

#Importing files that will be used for the project
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import pandas as pd

#States to examine: New Hampshire, California, Virgina, MaryLand, North Carolina, Georgia
#Look at Data for murders committed by men, women

class Graphs():

    def graph_year(self):
        self.__data = pd.read_csv('database.csv', low_memory=False)
        #Gathering the years to use as my x-axis and the murders for y-axis
        years, murders = [], []
        year = 1980
        #This loop here will push in each year to the years list as well as
        #get the murders for the specifed year and push it into a list.
        while year <= 2014:
            years.append(year)
            count = len(self.__data[self.__data.Year == year])
            murders.append(count)
            year += 1
        years = [dt.datetime.strptime(str(d),'%Y').date() for d in years]
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        # plt.ylim(14100,15200)
        plt.plot(years, murders)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Murders", fontsize=12)
        plt.title("Murders By Year", fontsize=24)
        plt.gcf().autofmt_xdate()
        plt.savefig('total_murders.png')
        plt.show()

    def graph_male(self):
        self.__data = pd.read_csv('database.csv', low_memory=False)
        #Gathering the years to use as my x-axis and the murders for y-axis
        years, murders = [], []
        year = 1980
        #This loop here will push in each year to the years list as well as
        #get the murders for the specifed year and push it into a list.
        while year <= 2014:
            years.append(year)
            count = len(self.__data[(self.__data.Year == year) & (self.__data.Perpetrator_Sex == 'Male')])
            murders.append(count)
            year += 1
        years = [dt.datetime.strptime(str(d),'%Y').date() for d in years]
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        plt.ylim(8200,15000)
        plt.plot(years, murders)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Murders", fontsize=12)
        plt.title("Male Murders: 1980-2014", fontsize=24)
        plt.gcf().autofmt_xdate()
        # plt.savefig('male_graph.png')
        plt.show()

    def graph_female(self):
        self.__data = pd.read_csv('database.csv', low_memory=False)
        #Gathering the years to use as my x-axis and the murders for y-axis
        years, murders = [], []
        year = 1980
        #This loop here will push in each year to the years list as well as
        #get the murders for the specifed year and push it into a list.
        while year <= 2014:
            years.append(year)
            count = len(self.__data[(self.__data.Year == year) & (self.__data.Perpetrator_Sex == 'Female')])
            murders.append(count)
            year += 1
        years = [dt.datetime.strptime(str(d),'%Y').date() for d in years]
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        #plt.ylim(8200,15000)
        plt.plot(years, murders, color='red')
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Murders", fontsize=12)
        plt.title("Female Murders: 1980-2014", fontsize=24)
        plt.gcf().autofmt_xdate()
        # plt.savefig('female_graph.png')
        plt.show()


# graph = Graphs()
#graph.graph_year()
# graph.graph_male()
# graph.graph_female()
