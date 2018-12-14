from itertools import combinations

# Read input file and create list of data
with open(".\input\input02.txt") as f:
  data = f.read().splitlines()

def duplicate(iterable):
    count = dict()
    for i in iterable:
        count[i] = count.get(i, 0) + 1
    return count

# The following is not an efficient method as it calls the duplicate function
# twice for each line instead of calling once and checking the 2's and 3's
doublet, triplet = 0, 0
for line in data:
    doublet += (2 in duplicate(line).values())
    triplet += (3 in duplicate(line).values())


# Returns number of matching letters
def match(str1, str2):
    count = 0
    for index in range(len(str1)):
        if str1[index] == str2[index]:
            count+=1
    return count

# Returns string without matching letter indexes
def name(str1, str2):
    string = ''
    for index in range(len(str1)):
        if str1[index] == str2[index]:
            string += str1[index]
    return string

pairwise = list(combinations(data, 2))

for pair in pairwise:
    if match(pair[0], pair[1]) == len(pair[0])-1:
        correct_pair = pair
        break

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(doublet * triplet))
  print("Solution to problem 2 is {}".format(name(correct_pair[0], correct_pair[1])))
