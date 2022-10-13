import numpy as np 
import random
import matplotlib.pyplot as plt 

figure, axis = plt.subplots(2, 3)   #splits the figure into six different figures

n=[1,2,5,10,20,50] 					#number of x values

m=[] 								#creates an array to put the mean values 
for i in range(len(n)):             #creates six different arrays in m
	m.append([])

for j in range(1000): 				#repeats 1000 times 
	n_1=[] 							#holds x values
	for i in range(len(n)):
		for j in range(n[i]):
			n_1.append(np.random.exponential()) #creates random numbers
		m[i].append(np.mean(n_1))   #calculates the mean of the values in n_1 and appends in m

for i in range(2): 					#loop for plotting the datas
	for j in range(3):
		if i==0:
			axis[i,j].hist(m[i+j],100)
			axis[i,j].set_title("n = {}".format(n[i+j]))
			axis[i,j].set_xlabel("Mean")
			axis[i,j].set_ylabel("Frequency")
		if i==1:
			axis[i,j].hist(m[i+j+2],100)
			axis[i,j].set_title("n=  {}".format(n[i+j+2]))
			axis[i,j].set_xlabel("Mean")
			axis[i,j].set_ylabel("Frequency")


plt.show()







