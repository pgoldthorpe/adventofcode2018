# Read input file and create list of data
with open(".\day02\input.txt") as f:
  data = f.read().splitlines()

def duplicate(iterable):
    """
    Returns a boolean tuple if the iterable contains two and three of the same element, respectively.

    Parameters
    ----------
    iterable : interable
            The iterable to be iterated over.

    Returns
    -------
    tuple : tuple
            A tuple containing the boolean response to the string having doublet or triplet of element.
    
    Examples
    --------
    >>> 'abc'
    (False, False)

    >>> 'aabb'
    (True, False)

    >>> 'aaabb'
    (True, True)

    >>> 'aaab'
    (False, True)
    """
    count = dict()
    for i in iterable:
        count[i] = count.get(i, 0) + 1
    return (2 in count.values(), 3 in count.values())

twos, threes = 0, 0
for line in data:
    twos += duplicate(line)[0]
    threes += duplicate(line)[1]

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(twos*threes))
  print("Solution to problem 2 is {}".format('hello'))
