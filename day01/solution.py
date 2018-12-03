with open("input.txt") as f:
  data = f.read().splitlines()

freq_list = [int(i) for i in data]

seen_freq = set()
value = 0
repeat = True

while repeat:
  for i in freq_list:
    value += i
    if value in seen:
      repeat = False
      break
    seen.add(value)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(sum(freq)))
  print("Solution to problem 2 is {}".format(val))