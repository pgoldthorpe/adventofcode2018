with open(".\input\input05.txt") as f:
  data = f.read().splitlines()

def polymer(chain):
    polymer = [' ']
    for i in chain:
        if abs(ord(polymer[-1]) - ord(i)) == 32:
            polymer.pop()
        else:
            polymer.append(i)
    return len(polymer[1:])

polymer_dict = {}
for i in range(65,91):
    string = data[0].replace(chr(i), "").replace(chr(i + 32), "")
    polymer_dict[chr(i)] = polymer(string)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(polymer(data[0])))
  print("Solution to problem 2 is {}".format(min(polymer_dict.values())))