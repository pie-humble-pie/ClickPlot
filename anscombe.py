import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def solve(X, Y):

  n = len(X)

  numerator = denominator = 0
  xmean = np.mean(X)
  ymean = np.mean(Y)

  for i in range(n):
    numerator += (X[i] - xmean) * (Y[i] - ymean)
    denominator += (X[i] - xmean) ** 2

  m = numerator/denominator
  c = ymean - m*xmean

  return m, c

def draw(quad, x, y):

  X = np.array([0,20])
  plt.subplot(2, 2, quad)
  plt.scatter(x, y)
  m, c = solve(x, y)
  plt.title("Slope = %f  Intercept = %f" % (m, c))
  plt.plot(X, m*X + c, "r-")

data = pd.read_csv('C:/Users/aryam/Desktop/MLALGO/data/anscombe.csv').values
x1,x2,x3,x4 = ([] for i in range(4))
y1,y2,y3,y4 = ([] for i in range(4))
for i in range(0,11):
    x1.append(data[i,1])
    y1.append(data[i,2])
for i in range(11,22):
    x2.append(data[i,1])
    y2.append(data[i,2])
for i in range(22,33):
    x3.append(data[i,1])
    y3.append(data[i,2])
for i in range(33,44):
    x4.append(data[i,1])
    y4.append(data[i,2])
plt.figure()
plt.xlim(0,20)
plt.ylim(0,20)
draw(1, x1, y1)
draw(2, x2, y2)
draw(3, x3, y3)
draw(4, x4, y4)
plt.show()
