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

fabric = create_matrix(1000,1000)
for line in data:
  m = re.search('expression', line)  # haven't figured out the expression to separate digits into groups
  _, x, y, w, h = map(int, m.groups())
  fabric = sheet(fabric, x, y, w, h)

# overlap = sum(i>1 for i in ... for j in ...)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(fabric)) # overlap
  print("Solution to problem 2 is {}".format('hello'))
