import datetime

with open(".\input\input04.txt") as f:
  data = f.read().splitlines()

data = sorted(data)

for i in data:
  print(i)