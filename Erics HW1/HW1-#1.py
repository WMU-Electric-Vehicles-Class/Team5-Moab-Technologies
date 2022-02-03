import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#setting plot spacing


plot1 = plt.subplot(331)
plot2 = plt.subplot(332)
plot3 = plt.subplot(333)
plot4 = plt.subplot(334)
plot5 = plt.subplot(335)
plot6 = plt.subplot(336)
plot7 = plt.subplot(337)
plot8 = plt.subplot(338)
plot9 = plt.subplot(339)

#txt is Time(s) - Velocity(mph)

#ftp2: The UN/ECE Elementary Urban Cycle is Part 1 of the ECE Type 1 Test.
#ftp3: The Highway Fuel Economy Driving Schedule (HWFET)
#ftp4: NYCCCOL.TXT	New York City Cycle

ftp2= np.loadtxt('ftp2.txt', dtype=float)
ftp3= np.loadtxt('ftp3.txt', dtype=float)
ftp4= np.loadtxt('ftp4.txt', dtype=float)


# (kph) vs (sec)
time_s2 = ftp2[:,0]
speed_kph2 = ftp2[:,1]*1.60934

time_s3 = ftp3[:,0]
speed_kph3 = ftp3[:,1]*1.60934

time_s4 = ftp4[:,0]
speed_kph4 = ftp4[:,1]*1.60934

# (miles/hour) vs (miles)
speed_mph2 = ftp2[:,1]
speed_mi_s2 = ftp2[2:,1]*0.000277778
distance_mi2 = np.cumsum(speed_mi_s2)

speed_mph3 = ftp3[:,1]
speed_mi_s3 = ftp3[2:,1]*0.000277778
distance_mi3 = np.cumsum(speed_mi_s3)

speed_mph4 = ftp4[:,1]
speed_mi_s4 = ftp4[2:,1]*0.000277778
distance_mi4 = np.cumsum(speed_mi_s4)

# (meter/s^2) vs. (sec)
speed_metersps2 = ftp2[:,1]*0.44704
accel_gs2 = np.diff(speed_metersps2, prepend=0)

speed_metersps3 = ftp3[:,1]*0.44704
accel_gs3 = np.diff(speed_metersps3, prepend=0)

speed_metersps4 = ftp4[:,1]*0.44704
accel_gs4 = np.diff(speed_metersps4, prepend=0)


plot1.plot(time_s2,speed_kph2)
plot1.set_title('1')

plot2.plot(time_s3,speed_kph3)
plot2.set_title('2')
  
plot3.plot(time_s4,speed_kph4)
plot3.set_title('3')

plot4.plot(distance_mi2, speed_mph2)
plot4.set_title('4')
  
plot5.plot(distance_mi3, speed_mph3)
plot5.set_title('5')
  
plot6.plot(distance_mi4, speed_mph4)
plot6.set_title('6')

plot7.plot(time_s2,accel_gs2)
plot7.set_title('7')
  
plot8.plot(time_s3,accel_gs3)
plot8.set_title('8')
  
plot9.plot(time_s4,accel_gs4)
plot9.set_title('9')

plt.tight_layout()
plt.show()