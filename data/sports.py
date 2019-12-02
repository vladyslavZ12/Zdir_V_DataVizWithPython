import csv
import matplotlib.pyplot as plt 

sport = ['Biathlon', 'Skating',]
Biathlon = []
Skating = []

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
            if row[2] == "Biathlon":
                print(" won a gold medal")
                Biathlon.append(row[7])
            elif row[2] == "Skating":
                print("won a silver medal")
                Skating.append(row[7])
                    
            print(line_count)
            line_count += 1


print(len(Biathlon), len(Skating))

quantity = [len(Biathlon), len(Skating)]
plot = plt.bar(sport, quantity)

for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % int(height), ha='center', va='bottom')


plt.bar(sport,quantity, color=['turquoise','salmon'])
plt.title("Each sport medal count")
plt.xlabel("")
plt.ylabel("Unit")
plt.show()