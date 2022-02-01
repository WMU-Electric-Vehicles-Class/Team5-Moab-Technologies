# Team5-Moab-Technologies

David Boktor. I've successfully opened the file and currently editing it. 

###################################################
########      EPA PLot                #############

Nic Brown... Here's some code...

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

ftp = pd.read_csv('ftpcol.csv')
hwy = pd.read_csv('hwycol.csv')
urban = pd.read_csv('uddscol.csv')

plt.plot(ftp['time'], ftp['kph'], label='ftp')
plt.plot(hwy['time'], hwy['kph'], label='hwy')
plt.plot(urban['time'], urban['kph'], linestyle = 'dashdot', label='udd')
plt.xlabel('[s]')
plt.ylabel('[kph]')
plt.title('US EPA: velocity vs time')
plt.legend()
plt.grid()

###################################################
