# Read input file and create list of data
with open("input.txt") as f:
  data = f.read().splitlines()

freq_list = [int(i) for i in data]

def find_duplicate_frequency(freq_list):
  """
  Return the first repeated value of cumulative frequency list.
  Repeats the list until a duplicate value is found.

  Parameters
  ----------
  freq_list : list
      Input list of integers.
  
  Returns
  -------
  duplicate_freq : int
      A single value containing the first repeated frequency.
  
  Example
  -------
  >>> find_duplicate_frequency([1, -1])
  0

  >>> find_duplicate_frequency([3, 3, 4, -2, -4])
  10
  """
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