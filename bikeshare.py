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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter desired city (Chicago, New York City, or Washington): ').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            break
        else:
            print('\nSorry I didn\'t get that.\n')

    # get user input for month (all, january, february, ... , june)
    list_of_months = ('all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october' 'november', 'december')
    while True:
        month = input('Please enter desired month (All, January, February, etc): ').lower()
        if month in list_of_months:
            break
        else:
            print('\nSorry I didn\'t get that.\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_the_week = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    while True:
        day = input('Please enter desired day of the week (all, Monday, Tuesday, etc): ').lower()
        if day in days_of_the_week:
            break
        else:
            print('\nSorry I didn\'t get that.\n')

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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name(locale='English').str.lower()
    df['Weekday'] = df['Start Time'].dt.day_name(locale='English').str.lower()
    if month != 'all':
        df = df[(month == df['Month'])]
    if day != 'all':
        df = df[(day == df['Weekday'])]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month with your search criteria: ')
    print(df['Month'].mode()[0])
    print('\n')

    # display the most common day of week
    print('The most common day of the week with your search criteria: ')
    print(df['Weekday'].mode()[0])
    print('\n')

    # display the most common start hour
    print('The most common start hour with your search criteria: ')
    print(df['Start Time'].dt.hour.mode()[0])
    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station with your search criteria: ')
    print(df['Start Station'].mode()[0])
    print('\n')

    # display most commonly used end station
    print('The most commonly used end station with your search criteria: ')
    print(df['End Station'].mode()[0])
    print('\n')

    # display most frequent combination of start station and end station trip
    print('The most frequent combinatino of start startion and end startion with your search criteria: ')
    print((df['Start Station'] + ' and ' + df['End Station']).mode()[0])
    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time in minutes with your search criteria: ')
    print(df['Trip Duration'].sum() / 60)
    print('\n')

    # display mean travel time
    print('The mean travel time in minutes with your search criteria: ')
    print(df['Trip Duration'].mean() / 60)
    print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of each user type with your search criteria: ')
    print(df['User Type'].value_counts())
    print('\n')

    # Display counts of gender
    if city != 'washington':
        print('Count of each gender with your search criteria: ')
        print(df['Gender'].value_counts())
        print('\n')
    else:
        print('Sorry but no gender stats can be calculated with Washington')

    # Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest year of birth with your search criteria: ')
        print(int(df['Birth Year'].min()))
        print('\n')

        print('The most recent year of birth with your search criteria: ')
        print(int(df['Birth Year'].max()))
        print('\n')

        print('The most common year of birth with your search criteria: ')
        print(int(df['Birth Year'].mode()))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print('\nSorry but no birth year stats can be calculated with Washington\n')
        print('-'*40)

def raw_data(df):
    x = 0
    while True:
        response = input("\nWould you like to see 5 additional rows of raw data? (Yes or No)").lower()
        if response == 'yes':
            x += 1
            print(df[x:x+5])
        elif response == 'no':
            break
        else:
            print('\nSorry I didn\'t get that')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
