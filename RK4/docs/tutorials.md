#Ejemplo de uso

Este es un ejemplo de uso de la aplicacion de este metodo a un sistema con las caracteristicas descritas; copiar en un ejecutable de python.

~~~

import numpy as np

import matplotlib.pyplot as plt

iConst = 1.0j

oOper = np.array([[0, 1], [1, 0]])

yInit = np.array([[1, 0], [0, 0]])

def dyn_generator(oper, state):
    \indent return -1.0j*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    k1 = h*func(oper,state)
    k2 = h* func(oper+ (h/2), state+ (k1/2))
    k3 = h* func(oper + (h/2), state + (k2/2))
    k4 = h*func(oper+h,state+k3)
    return state + (1/6)* (k1+2*k2+2*k3+k4)

times = np.linspace(0, 10, 100).astype(float)

h = times[1]-times[0]

yCopy = yInit.copy()

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

for tt in range(times.size):
    stateQuant00[tt] = (yInit[0,0]).real
    stateQuant11[tt] = (yInit[1,1]).real
    yN=rk4(dyn_generator,oOper,yInit,h)
    yInit = yN

#Grafica de la funcion

plt.style.use('_mpl-gallery')

plt.figure(figsize=(6, 3), dpi=150)
plt.plot(times,stateQuant00,label='Estado(0,0)',color='r')
plt.plot(times,stateQuant11,label='Estado(1,1)',color='b')

plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.legend()
plt.show()
~~~
