import csv

def white_csv(path, data):
  with open(path, "w") as f:
    writer = csv.writer(f)
    for row_data in data:
      print("data=", row_data)
      writer.writerow(row_data)
      
path = r"./data.csv"
data = [[1,2,3],[4,5,6],[7,8,9]]

write_csv(path, data)
