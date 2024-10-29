
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, delimiter = ',', skiprows = 2)

### Your code here ###
time = data[:, 0]
lead_signal = data[:, 1]
V1 = data[:, 2]
filter_order = 4
cutoff_frequency = 40
sample_frequency = 1 / np.mean(np.diff(time))
print(sample_frequency)

nyquist_rate = sample_frequency / 2
normal_cutoff = cutoff_frequency / nyquist_rate
butter_lead_signal = signal.butter(filter_order, normal_cutoff, 'low', output = 'sos')
filtered_lead_signal = signal.sosfilt(butter_lead_signal, lead_signal)

diff_signal = np.diff(filtered_lead_signal, n=1)

sqr_signal = np.square(diff_signal)

window_size = 50
moving_average_signal = np.convolve(sqr_signal, np.ones(window_size) / window_size, mode = 'same')

### Your code here ###
adjusted_time = time[1:]

# use matplot lib to generate a single
plt.figure(figsize=(12, 6))
plt.plot(adjusted_time, moving_average_signal, color = 'blue')
plt.title("EKG Lead Signal (MLII vs Time)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend()
plt.grid()
plt.show()