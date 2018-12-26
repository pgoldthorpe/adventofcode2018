from AOC import Advent

day1 = Advent(2018, 1)
data = list(map(int, day1.input_data))

def find_duplicate_frequency(freq_list):

  seen_freq = set()
  value = 0

  while True:
    for freq in freq_list:
      value += freq
      if value in seen_freq:
        return value
      seen_freq.add(value)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(sum(data)))
  print("Solution to problem 2 is {}".format(find_duplicate_frequency(data)))