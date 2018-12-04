import re

# Read input file and create list of data
with open(".\day03\input.txt") as f:
  data = f.read().splitlines()

def create_matrix(cols, rows):
    return [[0 for x in range(cols)] for y in range(rows)]

def sheet(matrix, x, y, w, h):
    for i in range(y, y+h):
        for j in range(x, x+w):
            matrix[i][j]+=1
    return matrix

def single_sheet(matrix, x, y, w, h):
    number = 0
    for i in range(y, y+h):
        for j in range(x, x+w):
            number += matrix[i][j]
    return number

fabric = create_matrix(1000,1000)
for line in data:
  _, _, x, y, _, w, h = re.split('x|,|:| ', line)
  fabric = sheet(fabric, int(x), int(y), int(w), int(h))

count = 0
for i in range(1000):
    count += sum(i>1 for i in fabric[i])

for line in data:
  _, id, _, x, y, _, w, h = re.split('x|,|:| |#', line)
  if single_sheet(fabric, int(x), int(y), int(w), int(h)) == int(w)*int(h):
      break

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(count))
  print("Solution to problem 2 is {}".format(id))