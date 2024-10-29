import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date, county, state, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    # Since the data is ordered, I just need to find the first spot where cases > 0 which I do through for loops
    first_case_rockingham = None
    first_case_harrisonburg = None
    for (date, county, state, cases, deaths) in data:
        # The statement below is used throughout the code and just limits the for loop to look at the Rockingham in Virginia
        if county == "Rockingham" and state == "Virginia" and cases > 0:
            first_case_rockingham = date
            break
    for (date, county, state, cases, deaths) in data:
        # The statement below is used throughout the code and just limits the for loop to look at the Harrisonburg city in Virginia
        if county == "Harrisonburg city" and state == "Virginia" and cases > 0:
            first_case_harrisonburg = date
            break

    print(f"\nDate Of First COVID Case In Rockingham County: {first_case_rockingham}")
    print(f"\nDate Of First COVID Case In Harrisonburg: {first_case_harrisonburg}")


def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # I make a simple for loop that only looks at the desired county and city. Then, I calculate the increment of cases
    # per day by making temporary variables that hold the current cases and the previous cases and then subtracting them.
    # I then hold the date where that number is the greatest and print it.
    previous_val_harrisonburg = 0
    greatest_val_harrisonburg = 0
    date_harrisonburg = ""
    previous_val_rockingham = 0
    greatest_val_rockingham = 0
    date_rockingham = ""
    for (date, county, state, cases, deaths) in data:
        if county == "Harrisonburg city" and state == "Virginia":
            val_change = cases - previous_val_harrisonburg
            if val_change > greatest_val_harrisonburg:
                greatest_val_harrisonburg = val_change
                date_harrisonburg = date
            previous_val_harrisonburg = cases

    for (date, county, state, cases, deaths) in data:
        if county == "Rockingham" and state == "Virginia":
            val_change = cases - previous_val_rockingham
            if val_change > greatest_val_rockingham:
                greatest_val_rockingham = val_change
                date_rockingham = date
            previous_val_rockingham = cases


    print(f"\nIn Harrisonburg, {date_harrisonburg}, was the day with the most amount of COVID cases. ")
    print(f"\nIn Rockingham County, {date_rockingham}, was the day with the most amount of COVID cases. ")


def third_question(data):
    # Write code to address the following question:Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.

    # I first make lists for the date and number of new cases for both harrisonburg and rockingham.
    # Doing this makes my code a bit cleaner and easier for me to understand.
    harrisonburg_cases = []
    rockingham_cases = []
    previous_val_harrisonburg = 0
    previous_val_rockingham = 0
    for (date, county, state, cases, deaths) in data:
        if county == "Harrisonburg city" and state == "Virginia":
            new_cases = cases - previous_val_harrisonburg
            harrisonburg_cases.append((date, new_cases))
            previous_val_harrisonburg = cases
        elif county == "Rockingham" and state == "Virginia":
            new_cases = cases - previous_val_rockingham
            rockingham_cases.append((date, new_cases))
            previous_val_rockingham = cases
    # Below, I make another method where I output the start and end dates of the 7-day period where the increase in cases was the worst.
    # I do this by inputting the list I made previously of the date and new cases of harrisonburg and rockingham.
    def worst_7_days(list):
        list_7_days = []
        i = 0
        next_sum = 0
        max_sum = 0
        start_date = ""
        end_date = ""
        # Then, I make a for loop which creates a new list by only inputting the new cases.
        for date, new_cases in list:
            list_7_days.append(new_cases)
            next_sum += new_cases
            # This makes it so that "list_7_days" is not greater than length 7 by removing the 0 index and subtracting
            # the 0 index cases from the sum
            if len(list_7_days) > 7:
                next_sum -= list_7_days[0]
                list_7_days.pop(0)
            # This checks if the current "list_7_days" contains the 7 day period which where the cases sum is the most.
            # I then update "max_sum" and save the start and end dates of this 7 day period.
            if len(list_7_days) == 7 and next_sum > max_sum:
                max_sum = next_sum
                start_date = list[i - 6][0]
                end_date = list[i][0]
            i += 1
        return start_date, end_date, max_sum
    # I pass the previously created "harrisonburg_cases" list which contains dates and new cases for harrisonburg.
    # Then, I make new variables as shown below which will hold the relevant values from "worst_7_days" method.
    harrisonburg_start_date, harrisonburg_end_date, harrisonburg_sum = worst_7_days(harrisonburg_cases)
    # I follow the same two comments above but for the rockingham_cases list
    rockingham_start_date, rockingham_end_date, rockingham_sum = worst_7_days(rockingham_cases)

    # I wasn't sure if you wanted me to find whether harrisonburg or rockingham had the worst 7 day period so
    # I compared both and tell you the answer.
    if harrisonburg_sum > rockingham_sum:
        print(f"\nHarrisonburg had a worse 7 day period than Rockingham")
    else:
        print(f"\nRockingham had a worse 7 day period than Harrisonburg")
    # The following two print statements tell the start date, end date, and sum of harrisonburg's worst 7 day period
    print(f"\nThe worst 7 day period for Harrisonburg was from {harrisonburg_start_date} - {harrisonburg_end_date}")
    print(f"\nHarrisonburg had {harrisonburg_sum} cases during the worst 7 day period")
    # The following two print statements tell the start date, end date, and sum of rockingham's worst 7 day period
    print(f"\nRockingham had {rockingham_sum} cases during the worst 7 day period")
    print(f"\nThe worst 7 day period for Rockingham was from {rockingham_start_date} - {rockingham_end_date}")


if __name__ == "__main__":
    data = parse_nyt_data('us-counties.csv')

    for (date, county, state, cases, deaths) in data:
        print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question:Use print() to display your responses.
    # What was the worst seven day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    third_question(data)

##########################

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
