import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

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

figure, axis = plt.subplots(2, 3)		#splits the figure into six different figures




_, bins, _ = axis[0,0].hist(mt1, 10, density=1, alpha=0.5) 
mu,sigma = stats.norm.fit(mt1)
best_fit_line = stats.norm.pdf(bins, mu, sigma)
axis[0,0].plot(bins, best_fit_line) 
axis[0, 0].set_title("MT1")	

axis[0,1].hist(mt2, bins=10)
axis[0,1].set_title("MT2")

axis[0,2].hist(fin, bins=10)
axis[0,2].set_title("FIN")

axis[1,0].hist(lab, bins=10)
axis[1,0].set_title("LAB")

axis[1,1].hist(hw, bins=10)
axis[1,1].set_title("HW")

axis[1,2].hist(att, bins=10)
axis[1,2].set_title("ATT")




plt.show()								#shows the figure

