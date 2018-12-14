# Read input file and create list of data
with open("./input/input01.txt") as f:
  data = f.read().splitlines()

freq_list = [int(i) for i in data]

def find_duplicate_frequency(freq_list):

  seen_freq = set()
  value = 0
  repeat = True

  while repeat:
    for freq in freq_list:
      value += freq
      if value in seen_freq:
        repeat = False
        break
      seen_freq.add(value)
  
  return value

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(sum(freq_list)))
  print("Solution to problem 2 is {}".format(find_duplicate_frequency(freq_list)))