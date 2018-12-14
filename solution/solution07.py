with open(".\input\input07.txt") as f:
  data = f.read().splitlines()

data = [(a[5], a[36]) for a in data]

def flatten_list(given_list):
    return set([pair for item in given_list for pair in item])

def remove_set_item(item, dictionary):
    for key in dictionary:
        if item in dictionary[key]:
            dictionary[key].remove(item)

total_nodes = flatten_list(data)

graph = dict()
for node in total_nodes:
    graph[node] = set()

for edge in data:
    graph[edge[1]].add(edge[0])

answer = ''

while len(graph) > 0:
    to_be_placed = sorted([item for item in graph if len(graph[item])==0])
    node = to_be_placed[0]
    answer += node
    graph.pop(node)
    remove_set_item(node, graph)

if __name__ == "__main__":
  print("Solution to problem 1 is {}".format(answer))
  print("Solution to problem 2 is {}".format("Hello"))