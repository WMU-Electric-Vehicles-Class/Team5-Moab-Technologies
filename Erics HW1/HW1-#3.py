import matplotlib.pyplot as plt
from datetime import date
import numpy as np

dates = [date(1881,1,1), date(1882,1,1), date(1895,1,1), date(1960,1,1,), date(1969,1,1,), date(2000,1,1) ,date(2021,1,1),]
min_date = date(1873, np.min(dates).month, np.min(dates).day)
max_date = date(2022, np.max(dates).month, np.max(dates).day)
 
labels = ['G. Trouve\n - 7mph', 'William Ayrton\n - 8mph', 'Andrew Riker\nVehicle\n - 12mph', 'GM Kadette Conversion\n - 30mph', 'GE Delta\n - 55mph', 'Nissan Hypermini\n - 62mph', 'Model S Plaid\n - 175mph']
# labels with associated dates
labels = ['{0:%Y}:\n{1}'.format(d, l) for l, d in zip (labels, dates)]

fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
_ = ax.set_ylim(-2, 1.75)
_ = ax.set_xlim(min_date, max_date)
_ = ax.axhline(0, xmin=0.05, xmax=0.95, c='black', zorder=1)
 
_ = ax.scatter(dates, np.zeros(len(dates)), s=120, c='black', zorder=2)
_ = ax.scatter(dates, np.zeros(len(dates)), s=30, c='black', zorder=3)

label_offsets = np.zeros(len(dates))
label_offsets[::2] = .5
label_offsets[1::2] = -1
for i, (l, d) in enumerate(zip(labels, dates)):
     _ = ax.text(d, label_offsets[i], l, ha='center', fontfamily='serif', fontweight='bold', color='black',fontsize=12)

stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3   
markerline, stemline, baseline = ax.stem(dates, stems, use_line_collection=True)
_ = plt.setp(markerline, marker=',', color='royalblue')
_ = plt.setp(stemline, color='royalblue')

# hide lines around chart
for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)
 
# hide tick labels
_ = ax.set_xticks([])
_ = ax.set_yticks([])
 
_ = ax.set_title('Major EV Top Speeds', fontweight="bold", fontfamily='serif', fontsize=16, color='black')