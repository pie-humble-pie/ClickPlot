import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def solve(data, ncat):

  I = data.shape[0]
  F = data.shape[1] - 1

  hypothesis = [[] for i in range(ncat)]

  for i in range(I):
    cat = int(data[i][-1]) - 1

    if len(hypothesis[cat]) == 0:
      hypothesis[cat] = data[i, :-1]
    else:
      for f in range(F):
        if hypothesis[cat][f] != data[i][f]:
          hypothesis[cat][f] = '?'

  return hypothesis


data = pd.read_csv("C:/users/aryam/desktop/mlalgo/data/zoo.csv").values

cat = ['Mammal', 'Bird', 'Reptile', 'Fish',
        'Amphibians', 'Insect', 'Other']

hypothesis = solve(data, len(cat))

print(" " * 40,"HYPOTHESIS")
print("-" * 100)
for i in range(len(cat)):
    space = ' ' * (10 - len(cat[i]))
    print(cat[i],space,hypothesis[i],sep = ' ')
print("-" * 100)
