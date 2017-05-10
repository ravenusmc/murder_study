
#This file will hold the class that will manipulate the data from data.csv file.

#Importing files that will be used for the project
import pandas as pd
import numpy as np


data = pd.read_csv('database.csv')

print(data.head())
