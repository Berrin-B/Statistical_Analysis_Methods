
import numpy as np
import matplotlib.pyplot as plt

mt1=[]                  #arrays for the datas
mt2=[]

data=np.loadtxt("data2.txt")    #loads the datas from the text file

for i in data:                  #appends the datas to the arrays
    mt1.append(i[0])
    mt2.append(i[1])

mt1=np.array(mt1)               #turns the datas to numpy arrays
mt2=np.array(mt2)    
    
n=len(mt1)                      # the number of datas
plt.scatter(mt1,mt2)            #scatters the datas

s_xy=np.sum(mt1*mt2)-((np.sum(mt1)*np.sum(mt2))/n)  #calculates s_xy
s_xx=np.sum(mt1**2)-(np.sum(mt1)**2/n)              #calculates s_xx
s_yy=np.sum(mt2**2)-(np.sum(mt2)**2/n)              #calculates s_yy
totalss=s_yy                #total sum of squares

beta=s_xy/s_xx              #calculates beta

mt1_mean=np.sum(mt1)/n              #calculates mean
mt2_mean=np.sum(mt2)/n

alpha=mt2_mean-beta*mt1_mean        #calculates alpha

plt.plot(mt1,alpha+beta*mt1)        #fits the plot

ssr=s_xy**2/s_xx                    #sum of squares for regression
ssr=round(ssr,2)
sse=s_yy-ssr                        #sum of squares for error
sse=round(sse,2)
msr=ssr                             #mean squares for regression
msr=round(msr,2)
mse=sse/(n-2)                       #mean squares for error
mse=round(mse,2)
f=msr/mse                           #calculates f
f=round(f,2)
r_2=ssr/(totalss)                   #calculates r^2

d = {"Regression": [1, ssr, msr,f], #prints the results
"Error": [n-2, sse, mse,''],
"Total": [n-1, 17.22, '',''] }
print ("{:<10} {:<10} {:<10} {:<10} {:<10} ".format('Source','df','SS','MS', 'F'))
for k, v in d.items():
    df, ss, ms ,f= v
    print ("{:<10} {:<10} {:<10} {:<10} {:<10}".format(k, float(df), float(ss), ms, f))
    
print("r^2=",r_2)

plt.show()


