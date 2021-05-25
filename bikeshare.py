import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city=''
    cities=CITY_DATA.keys()
    while city not in cities:
        city=input('Enter the city you want to explore:').lower()
        if city not in cities:
            print('Please enter again,there are no data related')
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','feburary','march','april','may','june','all']
    month=''
    while month not in months:
        month=input('Enter the month you want to explore:').lower()
        if month not in months:
            print('No related data in this month, please enter again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day=''
    while day not in days:
        day=input('Enter the weekday you want to explore:').lower()
        if day not in days:
            print('Please enter again, there must be something wrong')

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print('The most popular month is {}.'.format(popular_month))


    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print ('The most popular day is {}.'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('The most popular start hour is {}.'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['start_to_end'] = df['Start Station'].str.cat(df['End Station'], sep=' ')
    popular_start_to_end=df['start_to_end'].mode()[0]
    print('The most frequent combination of start station and end station trip is {}.'.format(popular_start_to_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    min, sec = divmod(total_duration, 60)
    hour, min = divmod(min, 60)
    print('The total trip durationis is {} hours {} minutes {} seconds.'.format(hour,min,sec))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    min,sec=divmod(mean_travel_time, 60)
    print('The mean travel time is {} minutes {} seconds.'.format(min,sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('The number of user types is {}.'.format(user_types))

    # TO DO: Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print('The counts of gender are {}.'.format(gender))
    except:
        print('There are no gender datas')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest=int(df['Birth Year'].min())
        most_recent=int(df['Birth Year'].max())
        most_common=int(df['Birth Year'].mode())
        print('The most recent year of birth is {},the earliest year of birth is {}, the most common year of birth is {}.'.format(most_recent,earliest,most_common))
    except:
        print('There is no data of birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    if view_data == 'yes':
        print(df.head())
    start_loc = 0
    while True:
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != 'yes':
            return
        start_loc += 5
        print(df.iloc[[start_loc,start_loc+5]])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
