import csv 

filename = "/Users/bavi/Documents/DataVizWheather/data/sitka_weather_2018_simple.csv"


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
 #   print(header_row)
    
  #  for index,column_header in enumerate(header_row):
  #      print(index, column_header)

    highTemp = [int(temp[5]) for temp in reader]
#for tem in header_row:
#   t = int(tem[5])
#   highTemp.append(t)

print(highTemp)
