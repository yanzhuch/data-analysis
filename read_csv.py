import csv

def read_csv(path):
  info_list = []
  with open(path, "r") as f:
    data = csv.reader(f)
    for row in data:
      print("row data=", row)
      info_list.append(row)
  return info_list

path = r"./data.csv"

read_csv(path)
