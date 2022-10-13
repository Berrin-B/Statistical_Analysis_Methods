import numpy as np
import math

mt1=[]									#arrays for the datas of the text file
mt2=[]
fin=[]
lab=[]
hw=[]
att=[]
data = np.loadtxt("data2.txt")			#loads the datas from the text file


for i in data:							#takes the columns from the text file and fills the arrays with this data
	mt1.append(i[0])
	mt2.append(i[1])
	fin.append(i[2])
	lab.append(i[3])
	hw.append(i[4])
	att.append(i[5])

def mean(list):							#function to calculate mean
	sum=0								#initially sum is zero
	for j in list:
		sum=sum+j						#sums every number in the list
	mean=sum/len(list)					#calculates the mean of the list
	return mean

def median(list):						#function to calculate median
	newlist=sorted(list)				#rearranges the list from smallest to largest number
	if (len(list)%2==0):				#checks if the length of the list is even or not
		a=[]
		a.append(newlist[(len(list)//2)-1])		#takes two numbers in the middle and appends a
		a.append(newlist[(len(list)//2)])
		m=(a[0]+a[1])/2.0						#calculates median
		return m
	else:
		m=newlist[(len(list)-1)//2]				#if the length of the list is odd, the median is the number in the middle
		return m

def s_deviation(list):					#function to calculate standart deviation
	m=mean(list)						#calculates the mean of the list
	for i in list:						#applies standart deviation formula
		b=[]
		b.append((m-i)**2)
	sum=0
	for j in b:
		sum=sum+j
	sd=math.sqrt((sum)/(len(list)-1))
	return sd

def skewness(list):						#function to calculate skewness
	skew=(3*(mean(list)-median(list)))/s_deviation(list)	#skewness formula
	if skew>0:												#if bigger than zero; positive skewness. if smaller than zero;negative skewness
		return "positive skew"
	if skew<0:
		return "negative skew"

print("Mean of each data set:", "midterm 1:",mean(mt1),"midterm 2:",mean(mt2),"final:",mean(fin),"lab:",mean(lab),"hw:",mean(hw),"attandance:",mean(att),sep="\n")                #prints the results
print("Median of each data set:","midterm 1:",median(mt1),"midterm 2:",median(mt2),"final:",median(fin),"lab:",median(lab),"hw:",median(hw),"attandance:",median(att),sep="\n")
print("Standart deviation of each data set:","midterm 1:",s_deviation(mt1),"midterm 2:",s_deviation(mt2),"final:",s_deviation(fin),"lab:",s_deviation(lab),"hw:",s_deviation(hw),"attandance:",s_deviation(att),sep="\n")
print("Direction of skew of each data set:","midterm 1:",skewness(mt1),"midterm 2:",skewness(mt2),"final:",skewness(fin),"lab:",skewness(lab),"hw:",skewness(hw),"attandance:",skewness(att),sep="\n")

