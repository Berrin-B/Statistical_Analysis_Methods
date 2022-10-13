import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

accidents=[0,1,2,3,4,5] 				#data sets
frequency=[447,132,42,21,3,2]

n=np.linspace(0.001,10,100) 			#creates array in range 0.001-10

def log_L(n): 							#calculates log_l
	return 15*np.log(n)-6*n-np.log(120*24*12)

def log_L_L(n):      					#calculates the derivative of log_l
	return (15/n)-6


x=[] 
for i in n: 							#applies the function log_l and adds the results in array
	x.append(log_L(i))

y=log_L_L(n) 							#applies the function log_l_l and adds the results in array

lam=[] 									
for k in range(len(y)): 				#finds the derivatives that are close to zero
	if -0.5<=y[k]<=0.5:
		lam.append(n[k])

def mean(list):							#function to calculate mean
	sum=0								#initially sum is zero
	for j in list:
		sum=sum+j						#sums every number in the list
	mean=sum/len(list)					#calculates the mean of the list
	return mean
	
print("lambda_ml=","-", mean(lam)-lam[0], mean(lam), "+", lam[-1]-mean(lam))

plt.plot(n,x)

plt.show()








