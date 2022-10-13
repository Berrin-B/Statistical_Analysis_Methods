import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.loadtxt("data.txt")	#loads the datas from the text file

s_price=[]						#empty arrays to fill with the datas
h_size=[]

for i in data:					#takes the columns from the text file and fills the arrays with this data
	s_price.append(i[1])
	h_size.append(i[2])

def mean(list):							#function to calculate mean
	sum=0								#initially sum is zero
	for j in list:
		sum=sum+j						#sums every number in the list
	mean=sum/len(list)					#calculates the mean of the list
	return mean

def s_deviation(list):					#function to calculate standart deviation
	m=mean(list)
	b=[]						#calculates the mean of the list
	for i in list:						#applies standart deviation formula
		b.append((m-i)**2)
	sum=0
	for j in b:
		sum=sum+j
	sd=np.sqrt((sum)/(len(list)))
	return sd

def confidence_int(list): 							#function to calculate confidence interval
	m_e=(1.96*s_deviation(list))/np.sqrt(len(list))  #calculates margain of error
	return m_e

m=[] 
for i in range(len(s_price)):
	m.append(s_price[i]/h_size[i])

n=[]
n.append(mean(m)*mean(h_size))       				#calculates average selling price usig price/house size in m^2

print("Average selling price using selling prices:",mean(s_price))  			#prints the results
print("Average selling price using prices/House size:", mean(n))
print("Margain of error:",confidence_int(s_price))
print("%95 Confidence interval:",mean(s_price)-confidence_int(s_price),"<μ<",mean(s_price)+confidence_int(s_price))


plt.hist(s_price, bins=10) 							#plots the histogram
plt.title("Histogram of Selling Prices")
plt.xlabel("Selling price")

plt.show() 											#shows the histogram





