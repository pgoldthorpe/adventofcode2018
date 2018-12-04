# Read input file and create list of data
with open(".\day02\input.txt") as f:
  data = f.read().splitlines()

def duplicate(iterable):
    count = dict()
    for i in iterable:
        count[i] = count.get(i, 0) + 1
    return count

doublet, triplet = 0, 0
for line in data:
    doublet += (2 in duplicate(line).values())
    triplet += (3 in duplicate(line).values())

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(doublet * triplet))
  print("Solution to problem 2 is {}".format('hello'))
