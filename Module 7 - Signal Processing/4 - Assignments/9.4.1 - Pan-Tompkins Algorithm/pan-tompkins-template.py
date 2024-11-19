import numpy as np
from ekg_testbench import EKGTestBench
from scipy import signal as sg
#import matplotlib.pyplot as plt


def detect_heartbeats(filepath):
    """
    Perform analysis to detect location of heartbeats
    :param filepath: A valid path to a CSV file of heart beats
    :return: signal: a signal that will be plotted
    beats: the indices of detected heartbeats
    """
    if filepath == '':
        return list()

    # import the CSV file using numpy
    path = filepath

    # load data in matrix from CSV file; skip first two rows
    data = np.loadtxt(path, delimiter=',', skiprows=2)

    # save each vector as own variable
    time = data[:, 0]
    lead_signal = data[:, 1]
    v1 = data[:, 2]
    filter_order = 4
    cutoff_frequency = 60
    sample_frequency = 1 / np.mean(np.diff(time))
    print(sample_frequency)

    # identify one column to process. Call that column signal

    # pass data through LOW PASS FILTER (OPTIONAL)
    nyquist_rate = sample_frequency / 2
    normal_cutoff = cutoff_frequency / nyquist_rate
    #butter_lead_signal = sg.butter(filter_order, normal_cutoff, 'low', output='sos')
    butter_lead_signal = sg.butter(filter_order, [30, 100], fs=sample_frequency, btype='band', output='sos')
    butter_signal = sg.sosfilt(butter_lead_signal, lead_signal)

    # pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result
    ## your code here

    # pass data through differentiator
    diff_signal = np.diff(butter_signal, n=1)

    # pass data through square function
    sqr_signal = np.square(diff_signal)
    print(sqr_signal)

    # pass through moving average window
    window_size = 50
    avg_signal = np.convolve(sqr_signal, np.ones(window_size) / window_size, mode='same')

    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result

    def peaks_height(signal):
        max_height = 0
        for val in signal:
            if val > max_height:
                max_height = val
        return max_height * 0.065
    print(peaks_height(avg_signal))

    peaks, _ = sg.find_peaks(avg_signal, height=peaks_height(avg_signal), distance=100)

    beats = peaks

    # do not modify this line
    return avg_signal, beats


# when running this file directly, this will execute first
if __name__ == "__main__":

    # place here so doesn't cause import error
    import matplotlib.pyplot as plt

    # database name
    database_name = 'mitdb_201'

    # set to true if you wish to generate a debug file
    file_debug = True

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = True

    ### DO NOT MODIFY BELOW THIS LINE!!! ###

    # path to ekg folder
    path_to_folder = "../../../data/ekg/"

    # select a signal file to run
    signal_filepath = path_to_folder + database_name + ".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = detect_heartbeats(signal_filepath)

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder + database_name + "_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks.tolist()
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plt of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
        plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
        plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")

