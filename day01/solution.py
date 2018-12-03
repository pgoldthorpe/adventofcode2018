with open("input.txt") as f:
  data = f.read().splitlines()

freq = [int(i) for i in data]

 
seen = set()
val = 0
cont = True

while cont:
  for i in freq:
    val += i
    if val in seen:
      print("duplicate found:", val)
      cont = False
      break
    seen.add(val)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(sum(freq)))
  print("Solution to problem 2 is {}".format(val))