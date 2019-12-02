import matplotlib.pyplot as plt
import csv
import numpy as np 
import pandas as pd

years = [1994,1998,2002,2006,2010,2014]
medals_one = []
medals_two = []
medals_three = []
medals_four = []
medals_five = []
medals_six = []

medals_one_s= []
medals_two_s= []
medals_three_s= []
medals_four_s = []
medals_five_s = []
medals_six_s = []
i = 0



categories = [] 

with open('data/ukrres - olimp.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("this iis the first. raw in the spreadsheet")
            categories.append(row)
            line_count += 1

        else:
            if row[0] == "1994":
                medals_one.append(row[0])
            elif row[0] == "1998":
                
                medals_two.append(row[0])
            elif row[0] == "2002":
                
                medals_three.append(row[0])
            elif row[0] == "2006":
                
                medals_four.append(row[0])
            elif row[0] == "2010":

                medals_five.append(row[0])
                
            elif row[0] == "2014":
                
                medals_six.append(row[0])
            
    
            
            print(line_count)
            line_count += 1


with open('data/svk - svk.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print("this iis the first. raw in the spreadsheet")
            categories.append(row)
            line_count += 1

        else:
            if row[0] == "1994":
                medals_one_s.append(row[0])
            elif row[0] == "1998":
                
                medals_two_s.append(row[0])
            elif row[0] == "2002":
                
                medals_three_s.append(row[0])
            elif row[0] == "2006":
                
                medals_four_s.append(row[0])
            elif row[0] == "2010":

                medals_five_s.append(row[0])
                
            elif row[0] == "2014":
                
                medals_six_s.append(row[0])
            
    
            
            print(line_count)
            line_count += 1

medal = [len(medals_one),len(medals_two),len(medals_three),len(medals_four),len(medals_five),len(medals_six)]
medals = [len(medals_one_s),len(medals_two_s),len(medals_three_s),len(medals_four_s),len(medals_five_s),len(medals_six_s)]

plt.plot(years, medal, color="c", linewidth=6.0)
plt.plot(years, medals, color="y", linewidth=6.0)


labels = "Ukraine", "Slovakia"
plt.legend(labels, loc=1)
plt.ylabel("medal quantity")
plt.xlabel("years")
plt.title("UKR results compared to bordering SVK ", pad=20)
plt.xlim(1990, 2018)
plt.ylim(0, 6)

plt.show()