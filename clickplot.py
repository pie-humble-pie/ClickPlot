import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def plot_hypothesis(X, Y, N):

     global ax1,ax2,r,R
     num = den = 0
     xm = np.mean(X)
     ym = np.mean(Y)

     for i in range(N):
         num += (X[i] - xm) * (Y[i] - ym)
         den += (X[i] - xm) ** 2

     m = num/den
     c = ym - m*xm
     R.append(Y[-1] - m*X[-1] - c)
     for i in range(N):
         if r[i] != 0:
            r[i].remove()
         r[i] = ax1.plot(np.array([X[i], X[i]]), np.array([Y[i], m*X[i]+c]), color="orange")[0]
         r[i].set_linestyle(':')
     ax2.scatter(X,R,color = 'orange')
     draw(m,c)

def draw(m,c):
    x = np.array([-200,200])
    l.set_xdata(x)
    l.set_ydata(m * x + c)
    l.set_linestyle('-')
    plt.draw()

def onclick(event):
    global X,Y,N,r
    X.append(event.xdata)
    Y.append(event.ydata)
    r.append(0)
    print("X = %d , Y = %d" %(X[-1],Y[-1]))
    ax1.scatter(X,Y,color = 'blue',label = 'Data Points')
    N += 1
    if N == 1:
        R.append(0)
    if N >= 2:
        plot_hypothesis(X,Y,N)

X = []
Y = []
r = []
R = []
N = 0
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set_xlim([-200,200])
ax1.set_ylim([-200,200])
ax2.set_xlim([-200,200])
ax2.set_ylim([-200,200])
ax1.get_figure().canvas.mpl_connect('button_press_event',onclick)
ax1.scatter(X,Y,color = 'blue',label = 'Data Points')
l = ax1.plot(X, Y, color="red", label = "Hypothesis")[0]
ax2.scatter(X,R,color = 'orange')
ax2.plot(np.arange(-200,200,1),np.zeros(400),color = 'blue')[0].set_linestyle(':')
ax1.set_title("Linear Regression Plot with Residues")
ax2.set_title("Residual Plot")
ax1.legend()
plt.show()
