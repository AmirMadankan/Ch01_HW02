import matplotlib.pyplot as plt

csv_file = open ("files/Ch01_HW02_csvFile.csv", 'r')
values = csv_file.read()
values = values.split(",")

n = len(values)
values_close = []
for i in range(16, n-6, 11):
    values_close.append(float(values[i]))

values_close.reverse()

m = len(values_close)
dy = []
for i in range(m-1):
    dy.append(values_close[i+1] - values_close [i])

yprime = dy

sets = []
for i in range(m-9):
    sets.append(values_close[i:i+10])

L = len(sets)
sets_predict = []
for i in range(L-1):
    if sets[i+1][9] > sets[i][9]:
        sets_predict.append(True)
    else:
        sets_predict.append(False)

plt.plot(values_close, label="chart")
plt.plot(yprime,label="dervative")
plt.legend()
plt.title("fameli from 2007 to 2022")
plt.xlabel("day")
plt.ylabel("price")
plt.show()