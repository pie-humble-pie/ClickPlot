import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def hypothesis(x,theta):
    return theta[0] + theta[1]*x


def gradient(X,Y,theta):

    grad = np.zeros((2,))
    m = len(X)
    hx = hypothesis(X[m-1],theta)
    grad[0] +=  (hx-Y[m-1])
    grad[1] += (hx-Y[m-1])*X[m-1]
    return grad


def gradientDescent(X,Y,theta,learning_rate = 0.001):
    grad = gradient(X,Y,theta)
    theta[0] = theta[0] - learning_rate*grad[0]
    theta[1] = theta[1] - learning_rate*grad[1]
    return theta

def plot_hypothesis(X, Y, N):

     global ax1,ax2,r,R,theta
     num = den = 0
     xm = np.mean(X)
     ym = np.mean(Y)
     gradientDescent(X,Y,theta)
     c = theta[0]
     m = theta[1]
     print(m)
     print(c)
     R.append(Y[-1] - m*X[-1] - c)
     for i in range(N):
         if r[i] != 0:
            r[i].remove()
         r[i] = ax1.plot(np.array([X[i], X[i]]), np.array([Y[i], m*X[i]+c]), color="orange")[0]
         r[i].set_linestyle(':')
     ax2.scatter(X,R,color = 'orange')
     draw(m,c)

def draw(m,c):
    x = np.array([-20,20])
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
    else:
        plot_hypothesis(X,Y,N)

X = []
Y = []
r = []
R = []
N = 0
theta = np.array([0.0, 0.0])
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.set_xlim([-20,20])
ax1.set_ylim([-20,20])
ax2.set_xlim([-20,20])
ax2.set_ylim([-20,20])
ax1.get_figure().canvas.mpl_connect('button_press_event',onclick)
ax1.scatter(X,Y,color = 'blue',label = 'Data Points')
l = ax1.plot(X, Y, color="red", label = "Hypothesis")[0]
ax2.scatter(X,R,color = 'orange')
ax2.plot(np.arange(-20,20,1),np.zeros(40),color = 'blue')[0].set_linestyle(':')
ax1.set_title("linear Regression using stochastic gradient descent")
ax2.set_title("residual plot")
ax1.legend()
plt.show()
