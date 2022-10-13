import numpy as np
import matplotlib.pyplot as plt


t=np.array([0,15,30,45,60,75,90,105,120,135])
N_i=[106,80,98,75,74,73,49,38,37,22]
y=np.array([4.663,4.382,4.585,4.317,4.304,4.290,3.892,3.638,3.611,3.091])
n=len(t)                #number of datas

m=np.mean(y)            #calculates mean
s=[]                    
for i in y:
    s.append(((i-m)**2)/n)
    
s=np.array(s)           #turns s into an array
    
alpha= (((np.sum(y/s))*(np.sum(t**2/s)))-(np.sum(t*y/s)*np.sum(t/s)))/(np.sum(1/s)*np.sum(t**2/s)-(np.sum(t/s))**2)  #calculates alpha
beta= ((np.sum(1/s)*np.sum(t*y/s))-(np.sum(t/s)*np.sum(y/s)))/((np.sum(1/s)*np.sum(t**2/s))-((np.sum(t/s))**2))      #calculates beta

lifetime=-1/beta        #calculates lifetime

s_b=(np.sum(1/s))/(np.sum(1/s)*np.sum(t**2/s)-(np.sum(t/s))**2)
s_t=np.sqrt(s_b)*(1/beta**2)

chi=np.sum(((N_i-np.exp(alpha)*np.exp(-t/lifetime))**2)/(np.exp(alpha)*np.exp(-t/lifetime))) #calculates chi square

dof=len(t)-2        #degree of freedom
prob=chi/dof
plt.plot(t,alpha+beta*t)   #does the fit



plt.scatter(t,y)        #plots the graph

print("lifetime=",lifetime,"±",s_t)
print("chi square:",chi)
print("probability:",prob)

plt.show()


