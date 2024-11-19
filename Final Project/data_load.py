import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'C:/Users/leonp/OneDrive/Documents/trashFile/battery20.csv'
data = pd.read_csv(file_path)

# Extract relevant columns
time = data['time']
battery_voltage = data['voltage_charger']
load_voltage = data['voltage_load']
load_current = data['current_load']

# Calculate the index range for the adjusted time window
start_index = int(len(time) * 0.1)  # Start at 10% of total data
end_index = int(len(time) * 0.2)    # Include only 10% of total data

# Slice the data to include only the 10% time window
time = time[start_index:end_index].reset_index(drop=True)
battery_voltage = battery_voltage[start_index:end_index].reset_index(drop=True)
load_voltage = load_voltage[start_index:end_index].reset_index(drop=True)
load_current = load_current[start_index:end_index].reset_index(drop=True)

# Create the plots
plt.figure(figsize=(14, 6))

# Plot 1: Time vs Battery Voltage
plt.subplot(1, 2, 1)
plt.plot(time, battery_voltage, label="Battery Voltage (V)", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Battery Voltage (V)")
plt.title("Time vs Battery Voltage")
plt.legend()

# Plot 2: Battery Voltage vs Load Voltage and Load Current
plt.subplot(1, 2, 2)
plt.plot(battery_voltage, load_voltage, label="Load Voltage (V)", color='green')
plt.plot(battery_voltage, load_current, label="Load Current (A)", color='red')
plt.xlabel("Battery Voltage (V)")
plt.ylabel("Load Voltage / Load Current")
plt.title("Battery Voltage vs Load Voltage and Current")
plt.legend()

plt.tight_layout()
plt.show()