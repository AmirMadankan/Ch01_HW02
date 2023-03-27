import matplotlib.pyplot as plt

csv_file = open ("files/Ch01_HW02_csvFile.csv", 'r')
values = csv_file.read()
values = values.split(",")
n = len(values)
values_close = []
for i in range(16, n-6, 11):
    values_close.append(float(values[i]))

values_close.reverse()

day = list(range(1,len(values_close)+1))
plt.plot(day, values_close)
plt.title("fameli from 2007 to 2022")
plt.xlabel("day")
plt.ylabel("price")
plt.show()
