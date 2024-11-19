import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sg

# Import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# Load data in matrix from CSV file; skip first two rows
data = np.loadtxt(path, delimiter=',', skiprows=2)

# Extract time and signal columns
time = data[:, 0]
lead_signal = data[:, 1]
V1 = data[:, 2]
filter_order = 4
cutoff_frequency = 60
sample_frequency = 1 / np.mean(np.diff(time))
print(sample_frequency)

# identify one column to process. Call that column signal

# pass data through LOW PASS FILTER (OPTIONAL)
nyquist_rate = sample_frequency / 2
normal_cutoff = cutoff_frequency / nyquist_rate
butter_lead_signal = sg.butter(filter_order, normal_cutoff, 'low', output='sos')
#butter_lead_signal = sg.butter(filter_order, [30, 100], fs=sample_frequency, btype='band', output='sos')
butter_signal = sg.sosfilt(butter_lead_signal, lead_signal)

# Plot filtered signal
plt.plot(time, V1, color='blue')
plt.title("Normal EKG Lead Signal (MLII vs Time)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend(['Filtered Signal'])
plt.grid()
plt.show()

plt.plot(time, butter_signal, color='blue')
plt.title("Filtered EKG Lead Signal (MLII vs Time)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude (mV)")
plt.legend(['Filtered Signal'])
plt.grid()
plt.show()