import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""
signal = np.loadtxt(signal_filepath, delimiter = ',', skiprows = 2)
## YOUR CODE HERE ##

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""
time = signal[:, 0]
lead_signal = signal[:, 1]
## YOUR CODE HERE ##

diff_signal = np.diff(lead_signal, n=1)



"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
sqr_signal = np.square(diff_signal)

"""
Step 5: Pass a moving filter over your data
"""
window_size = 50
moving_average_signal = np.convolve(sqr_signal, np.ones(window_size) / window_size, mode = 'same')

## YOUR CODE HERE
adjusted_time = time[1:]

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

# Original signal
axs[0].plot(time, lead_signal, color="blue")
axs[0].set_title("Original EKG Signal")
axs[0].set_ylabel("Amplitude")

# Differentiated signal
axs[1].plot(adjusted_time, diff_signal, color="green")
axs[1].set_title("Differentiated Signal")
axs[1].set_ylabel("Amplitude")

# Squared signal
axs[2].plot(adjusted_time, sqr_signal, color="orange")
axs[2].set_title("Squared Signal")
axs[2].set_ylabel("Amplitude")

# Moving average signal
axs[3].plot(adjusted_time, moving_average_signal, color="red")
axs[3].set_title("Moving Average of Squared Signal")
axs[3].set_xlabel("Time (s)")
axs[3].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()

