import datetime

with open(".\day04\input.txt") as f:
  data = f.read().splitlines()

data = sorted(data)

for i in data:
  print(i)