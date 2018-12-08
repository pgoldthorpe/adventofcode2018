with open(".\day05\input.txt") as f:
  data = f.read().splitlines()

def polymer(chain):
    polymer = [' ']
    for i in chain:
        if abs(ord(polymer[-1]) - ord(i)) == 32:
            polymer.pop()
        else:
            polymer.append(i)
    return len(polymer[1:])

minimize = []
for i in range(65,91):
    string = data[0].replace(chr(i),"").replace(chr(i+32),"")
    minimize.append(polymer(string))

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(polymer(data[0])))
  print("Solution to problem 2 is {}".format(min(minimize)))