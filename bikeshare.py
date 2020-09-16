import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
FIRST_SIX_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
LAST_SIX_MONTHS = ['july', 'august', 'september', 'october', 'november', 'december']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:   
        city = input("Please enter city name choosing from [Chicago, New York City ,Washington] : ").lower()
        if city in CITY_DATA:
            print("You selected ",city)
            break
        else :
            print("invalid city name, please enter a correct city name")
    print('-'*40)

    while True:
        month = input("Please enter the month you want to use to filter data from \n['january', 'february', 'march', 'april', 'may', 'june'] \nOr enter 'all' if you do not want to filter using month : ").lower()
        if month in FIRST_SIX_MONTHS:
            print("You selected ",month)
            break
        elif month == 'all':
              print("You selected no filter")
              break
        elif month in LAST_SIX_MONTHS:
            print("Unfortunately we only have data for the first six months of 2017, Please enter the month again : ")
        else:
            print("invalid input, please enter the month again : ")
    print('-'*40)

    while True:
        day = input("Please enter the day you want to use to filter data from \n['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] \nOr enter 'all' if you do not want to filter using day : ").lower()
        if day in DAYS:
            print("You selected ",day)
            break
        elif day == 'all':
              print("You selected no filter")
              break
        else:
            print("invalid input, please enter the day again : ")
   

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = FIRST_SIX_MONTHS
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    
    print("most common month : {}".format(FIRST_SIX_MONTHS[popular_month - 1]).title())
    print("most common day : {}".format(popular_week))
    print("most common hour : {}".format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].value_counts()
    try:
        popular_start_station_key = popular_start_station.keys().tolist()[0]
        popular_start_station_count = popular_start_station.tolist()[0]
        print("most common start station : {} , count : {}".format(popular_start_station_key, popular_start_station_count))
    except IndexError:
        print("most common start station data not found")
       
#     Or we can use this to get the mode which is the most commonly used start station

#     popular_start_station = df['Start Station'].mode()[0]
#     print("most common start station : {}".format(popular_start_station))


    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].value_counts()
    try:
        popular_end_station_key = popular_end_station.keys().tolist()[0]
        popular_end_station_count = popular_end_station.tolist()[0]
        print("most common end station : {} , count : {}".format(popular_end_station_key, popular_end_station_count))
    except IndexError:
        print("most common end station data not found")
        
#     Or we can use this to get the mode which is the most commonly used end station

#     popular_end_station = df['End Station'].mode()[0]
#     print("most common end station : {}".format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip


    popular_start_to_end_station = "From " + df["Start Station"] + " To " + df["End Station"]
    popular_start_to_end_station = popular_start_to_end_station.value_counts()
    try:
        popular_start_to_end_station_key = popular_start_to_end_station.keys().tolist()[0]
        popular_start_to_end_station_count = popular_start_to_end_station.tolist()[0]
        print("most common start to end station : {} , count : {}".format(popular_start_to_end_station_key, popular_start_to_end_station_count))
    except IndexError:
        print("most common end station data not found")
        
#     Or we can use this to get the mode which is the most commonly used start and end station

#     popular_start_to_end_station = "From " + df["Start Station"] + " To " + df["End Station"]
#     print("most common combination of start station and end station : {}".format(popular_start_to_end_station.mode()[0]))

    # Note: using mode get less time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if "Trip Duration" in df.keys().tolist():
        # TO DO: display total travel time
        total_travel_time = df['Trip Duration'].sum()

        # TO DO: display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
    
        print("Total travel time : {}".format(total_travel_time))
        print("Mean travel time : {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if "User Type" in df.keys().tolist():
        user_types = df["User Type"].value_counts()
        user_types_keys = user_types.keys().tolist()
        user_types_values = user_types.tolist()
        for user_type, value in zip(user_types_keys, user_types_values) :
            print("{} count is {}".format(user_type,value))
    
    print('-'*40)

    # TO DO: Display counts of gender
    if "Gender" in df.keys().tolist():
        user_gender = df["Gender"].value_counts()
        user_gender_keys = user_gender.keys().tolist()
        user_gender_values = user_gender.tolist()
        for gender, value in zip(user_gender_keys, user_gender_values) :
            print("{} count is {}".format(gender,value))
    else:
        print("No gender data")
    # TO DO: Display earliest, most recent, and most common year of birth
    print('-'*40)
    if "Birth Year" in df.keys().tolist():
        print("Earliest year of birth : ", df["Birth Year"].min())
        print("Most recent year of birth : ",df["Birth Year"].max())
        print("Common year of birth : ",df["Birth Year"].mode()[0])
    else :
        print("No birth year data")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    while True:
        choice = input('Would you like to read some of the raw data? Yes/No ').lower()
        if choice=='yes':
            choice=True
            break
        elif choice=='no':
            choice=False
            break
        else:
            print('Invalid input')

    if choice:
        index = df.index
        number_of_rows = len(index)
        count = 0
        invalid = False
        while True:
            for i in range(5):
                if number_of_rows > (i + count):
                    if not invalid:
                        print(df.iloc[i + count])
                        print()
                else:
                    print("data Ended")
                    break
            choice = input('Another five? Yes/No ').lower()
            if choice=='yes':
                count += 5
                invalid = False
                continue
            elif choice=='no':
                break
            else:
                invalid = True
                print('Invalid input')
                
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
