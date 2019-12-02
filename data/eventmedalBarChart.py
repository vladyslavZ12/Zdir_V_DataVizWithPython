import csv
import matplotlib.pyplot as plt 

sport = ['4x6KM Relay', '7.5KM', '15KM', 'Ice Dancing', 'Individual']
KMRelay = []
metres = []
KM = []
IceDancing = []
Individual= []

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
            if row[6] == "4X6KM Relay":
                print(" won a gold medal")
                KMRelay.append(row[7])
            elif row[6] == "7.5KM":
            	print("won a silver medal")
            	metres.append(row[7])
            elif row[6] == "15KM":
                print("won a silver medal")
                KM.append(row[7])
            elif row[6] == "Ice Dancing":
                print("won a silver medal")
                IceDancing.append(row[7])
            elif row[6] == "Individual":
                print("won a silver medal")
                Individual.append(row[7])

            
            print(line_count)
            line_count += 1


print(len(KMRelay), len(metres), len(KM), len(IceDancing), len(Individual))

quantity = [len(KMRelay), len(metres), len(KM), len(IceDancing), len(Individual)]
plot = plt.bar(sport, quantity)

for value in plot:
    height = value.get_height()
    plt.text(value.get_x() + value.get_width()/2.,
             1.002*height,'%d' % int(height), ha='center', va='bottom')




plt.title("Each sport event medal")
plt.xlabel("Sport")
plt.ylabel("Medals")



plt.title("Each sport event medal")
plt.xlabel("")
plt.ylabel("Unit")
plt.show()