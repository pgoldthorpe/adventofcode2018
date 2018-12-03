with open("input.txt") as f:
  data = f.read().splitlines()
  
if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(sum([int(i) for i in data])))

print("hello")
