import numpy as np
import matplotlib.pyplot as plt

x_1=[]                          #empty arrays
y_1=[]

x_2=[]
y_2=[]

for i in range (10000):         #generates 10000 random numbers between 0-1
    x1=np.random.uniform()
    x2=np.random.uniform()   
    x_1.append(x1)              #appends random numbers to the arrays
    x_2.append(x2)
    

for i in x_1:                   #calculates y and appends to the list
    y_1.append((-1/2)*(np.log(i*(1-np.exp(-2)))))
    
for k in x_2:
    y_2.append(k**(1/3))
    

figure, axis = plt.subplots(2, 2)
axis[0,0].hist(x_1)                     #plots histograms
axis[0,1].hist(y_1)
axis[1,0].hist(x_2)
axis[1,1].hist(y_2)
plt.show()
    

