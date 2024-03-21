import csv 

import matplotlib.pyplot as plt

filename = "/Users/bavi/Documents/DataVizWheather/Whether-data-visulatization/data/sitka_weather_2018_simple.csv"


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
  #  for index,column_header in enumerate(header_row):
  #      print(index, column_header)

    highs = [int(temp[5]) for temp in reader]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c = 'red')

#Format Plot
plt.title("Daily high temperatures, July 2018", fontsize =24)
plt.xlabel('', fontsize =16)
plt.ylabel("Tempature (F)", fontsize =16)
plt.tick_params(axis = 'both', which ='major', labelsize =16)

plt.show()

# print(highs)
