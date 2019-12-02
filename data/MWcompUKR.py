import csv
import matplotlib.pyplot as plt 

men = []
women = []


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
            if row[5] == "Men":
                print(" won a gold medal")
                men.append(row[7])
            elif row[5] == "Women":
            	print("won a silver medal")
            	women.append(row[7])
            
            print(line_count)
            line_count += 1


print(len(men), "men")
print(len(women), "women")


labels = ['men', 'women']
sizes = [len(men), len(women)]
color = ['deepskyblue', 'pink']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=color,  autopct='%.1f%%',shadow=True, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Men VS Women")
plt.xlabel("Medal Counts since 1924")
plt.show()