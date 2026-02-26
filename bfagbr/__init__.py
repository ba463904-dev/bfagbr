def is_proper_coloring(graph, coloring):
  for edge in graph.edges():
    if coloring[edge[0]]==coloring[edge[1]]:
      return False
  return True

def is_3_colorable(graph):
  n = graph.order()
  colorings = product([0,1,2], repeat = n)
  for coloring in colorings:
    if is_proper_coloring(graph, coloring):
      return coloring
  return False


##############################################

import itertools

def sum_of_values(values, keys):
    sum = 0
    n = len(values)
    for i in range(n):
        sum+=values[i]*keys[i]
    return sum

def knapsack_problem(profits, weights, capacity, goal):
    n = len(profits)
    sequences = itertools.product([0, 1], repeat = n)
    for sequence in sequences:
        if sum_of_values(weights, sequence) <= capacity: 
            if sum_of_values(profits, sequence)>=goal:
                return sequence
    return False
