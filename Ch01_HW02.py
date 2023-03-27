csv_file = open ("files/Ch01_HW02_csvFile.csv", 'r')
values = csv_file.read()
values = values.split(",")
n = len(values)
values_close = []
for i in range(16, n-6, 11):
    values_close.append(float(values[i]))

values_close.reverse()
print(values_close)