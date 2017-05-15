#This file will hold the class that will manipulate the data from murder.csv file.
#It will not actually run in the program but provide me with the code to make the
#graph images which I will insert into the program

#Importing files that will be used for the project
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np
import pandas as pd

class Graphs():

    def graph_year(self):
        self.__data = pd.read_csv('project/murder.csv', low_memory=False)
        #Gathering the years to use as my x-axis and the murders for y-axis
        years, murders = [], []
        year = 2011
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
        plt.ylim(14100,15200)
        plt.plot(years, murders)
        plt.gcf().autofmt_xdate()
        #plt.savefig('test.png')
        plt.show()


graph = Graphs()
graph.graph_year()

#CODE TO SAVE THE GRAPH AS AN IMAGE
# fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
# ax.plot([0,1,2], [10,20,3])
# fig.savefig('test.png')   # save the figure to file
# plt.close(fig)


# plt.xlabel("Year", fontsize=14)
# plt.ylabel("Murders", fontsize=12)
# plt.title("Murders By Year", fontsize=24)
# #This variable controls the width of the bars
# width = 1
# #This controls the width of the x-axis
# plt.xlim(2011,2015)
# #This controls the width of the y-axis
# plt.ylim(14100,15200)
# plt.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
# #Plotting the bar graph
# plt.bar(years, murders, width, color="blue")
# #This will display the bar graph
# plt.savefig('test.png')
# plt.show()
