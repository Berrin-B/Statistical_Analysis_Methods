import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from math import log
from math import e
from math import factorial

no_events=[0,1,2,3,4,5,6,7,8,9]							#number of events
no_intervals=[1042,860,307,78,15,3,0,0,0,1]				#number of intervals

figure, axis = plt.subplots(1, 2)						#creates two graphs

axis[0].bar(no_events,no_intervals,label="data") 		#plots the graph
plt.xlabel('Number of events')							#names the axis
plt.ylabel('Number of intervals')
axis[1].bar(no_events,no_intervals, label="data")		#plots the second graph
axis[1].set_yscale('log')								#y axis becomes logarithmic
axis[0].legend()										#creates legend
axis[1].legend()

x=0
for i in no_events: 									
        x=x+no_intervals[i]*i

y=0
for i in no_intervals:
	y=i+y

alpha=x/y 												#calculates alpha

p=[]													#creates empty array
for i in no_events:
	p.append((((alpha**i)*(e**(-alpha)))/factorial(i))*y)	#applies the poisson formula

axis[0].plot(no_events,p, "ro", label="expected")			#plots poisson distribution
axis[1].plot(no_events,p, "ro", label="expected")
axis[0].legend()											#adds legend
axis[1].legend()

print(p)
print(alpha)
plt.show()

	
