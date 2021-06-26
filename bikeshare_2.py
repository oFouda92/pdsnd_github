import pandas as pd

CITY_DATA = {'chicago': '/Users/omarfouda/Downloads/bikeshare-2/chicago.csv',
             'nyc': '/Users/omarfouda/Downloads/bikeshare-2/new_york_city.csv',
             'washington': '/Users/omarfouda/Downloads/bikeshare-2/washington.csv'}


def get_filters():

    print('Hello! Let\'s explore some US bike share data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Which city do you want to explore it's data? Choose from (chicago, washington, nyc)")
        city = input().lower()
        if city not in ("chicago", "nyc", "washington"):
            print("Invalid answer")
            continue
        else:
            break
    while True:
        print("Which month do you want to explore? Choose (january, february, march, april, may, june or all)")
        month = input().lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Invalid answer")
            continue
        else:
            break
    while True:
        print("Which day do you want to explore? Choose (sunday, monday, tuesday, wednesday, thursday, friday, saturday or all)")
        day_of_week = input().lower()
        if day_of_week not in ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"):
            print("Invalid answer")
            continue
        else:
            break

    print("You chose the city of ({}), the month of ({}) and the day of ({})".format(city, month, day_of_week))
    return city, month, day_of_week


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.day

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # display the most common month

    print("The most common month is: ", df['month'].mode()[0])

    # display the most common day of week

    print("The most common day is: ", df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    print("The most common hour is: ", df['hour'].mode()[0])
    print("_" * 200)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    print("The most common start station is: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most common end station is: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start And End Station'] = df['Start Station'] + df['End Station']
    print("The most common start and end station combination is: ", df['Start And End Station'].mode()[0])
    print("_" * 200)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    print("Total travel time is: ", df['Trip Duration'].sum())
    # display mean travel time
    print("Average travel time is: ", df['Trip Duration'].mean())
    print("_" * 200)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # Display counts of user types
    print("User types count is: ", df['User Type'].value_counts())
    # Display counts of gender
    if 'Gender' in df.columns:
        print("Gender count is: ", df['Gender'].value_counts())
    else:
        print("There is no Gender info for this city")
    if 'Birth Year' in df.columns:
        print("Earliest birth year is: ", df['Birth Year'].min().astype(int))
        print("Most recent birth year is: ", df['Birth Year'].max().astype(int))
        print("Most common birth year is: ", df['Birth Year'].mode()[0].astype(int))
    else:
        print("There is no Birth Year info for this city")


def display_data(df):
    index = 0
    user_input = input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes', 'y', 'yep', 'yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()


def main():

    while True:
        city, month, day = get_filters()
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()

