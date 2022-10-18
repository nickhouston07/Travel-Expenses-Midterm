VEHICLE_EXPENSE = 0.27
TAXI_LIMIT = 10
HOTEL_LIMIT = 90
BREAKFAST_LIMIT = 9
LUNCH_LIMIT = 12
DINNER_LIMIT = 16
PARKING_LIMIT = 6

def main():
    # Total cost default is 0 until other costs are added to it
    total_cost = 0

    # Get the length of the trip in days
    days = days_on_trip()
    print()

    # Gets the departure time, arrival time, and whether the times
    # were am or pm
    depart, arrival, ampm_depart, ampm_arrive = departure_arrival()
    print()

    # Addso the airfare cost, if any, to the total cost
    total_cost += round_trip_airfare()
    print()

    # Adds the rental cost, if any, to the total cost
    total_cost += car_rentals()
    print()

    # If a personal vehicle was driven, adds the fuel cost
    # to the total cost
    total_cost += miles_driven()
    print()

    # Adds the parking fee total, if any, to the total cost
    total_cost += parking_fees(days)
    print()

    # Adds the taxi fee total, if any, to the total cost
    total_cost += taxi_fees(days)
    print()

    # Adds the seminar/conference registration fee total,
    # if any, to the total cost
    total_cost += registration_fees()
    print()

    # Adds the hotel cost to the total cost
    total_cost += hotel_expenses(days)
    print()

    # Adds the meal expense to the total cost
    total_cost += meal_expenses(days, depart, arrival, ampm_depart, ampm_arrive)
    print()

    # Display the total cost
    print('The total cost of your trip is $', format(total_cost, ',.2f'),
          sep='')
    
    
def days_on_trip():
    # Get the number of days the trip was and ensure it is not less than 1
    days = int(input('How long, in calendar days, was your trip? '))
    while days < 1:
        print('Trip cannot be less than one day.')
        days = int(input('Enter length in days of your trip: '))
        
    return days

def departure_arrival():
    # Get the departure time and ensure it is a valid time
    depart = float(input('What time did you depart on your trip? '))
    while depart < 1 or depart > 12:
        print('Invalid time')
        depart = float(input('Enter departure time between 12 am' +
                                ' on the day you left and 12 am the next day'))
    ampm_depart = input('a.m.? or p.m.? ')

    # Get the arrival time and ensure it is a valid time
    arrival = float(input('What time did you arrive from your trip? '))
    while arrival < 1 or arrival > 12:
        print('Invalid time')
        arrival = float(input('Enter arrival time between 12 am' +
                                ' on the day you left and 12 am the next day'))
    ampm_arrive = input('a.m.? or p.m.? ')

    # Return the values
    return depart, arrival, ampm_depart, ampm_arrive

def round_trip_airfare():
    # Default flight cost is 0 so that it won't affect total cost
    # unless they answer yes to flying and enter an amount
    flight_cost = 0

    # Ask user if they flew and how much it cost
    print('Did you fly on your trip?')
    fly = input('Enter y for yes or anything else for no: ')
    if fly == 'y' or fly == 'Y':
        flight_cost = float(input('Enter the total cost of your flights: '))
        # Prevents negative cost amounts
        while flight_cost < 0:
            print('Flight cost cannot be less than 0')
            flight_cost = float(input('Re-enter the total cost of your flights: '))

    return flight_cost

            
def car_rentals():
    # Default rental cost is 0 so that it won't affect total cost
    # unless they answer yes to renting a vehicle and enter an amount
    rental_cost = 0

    # Ask user if they rented a vehicle and how much it cost
    print('Did you rent a vehicle on your trip?')
    rent = input('Enter y for yes or anything else for no: ')
    if rent == 'y' or rent == 'Y':
        rental_cost = float(input('Enter the total cost of your rental: '))
        # Prevents negative cost amounts
        while rental_cost < 0:
            print('Rental cost cannot be less than 0')
            rental_cost = float(input('Re-enter the total cost of your rental: '))

    return rental_cost
    

def miles_driven():
    # Default fuel cost is 0 so that it won't affect total cost
    # unless they answer yes to driving their own vehicle and enter an amount
    fuel_cost = 0

    # Ask user if they drove a peronal vehicle and how many miles they drove
    print('Did you drive a personal vehicle on your trip?')
    personal_vehicle = input('Enter y for yes or anything else for no: ')
    if personal_vehicle == 'y' or personal_vehicle == 'Y':
        miles = float(input('Enter the total miles driven: '))
        # Prevents negative miles amounts
        while miles < 0:
            print('Miles cannot be less than 0')
            miles = float(input('Re-enter the total miles: '))
        fuel_cost = miles * VEHICLE_EXPENSE

    return fuel_cost


def parking_fees(days):
    # Default parking fee cost is 0 so that it won't affect total cost
    # unless they answer yes to having parking fees and enter an amount
    parking_cost = 0

    # Parking allowance for trip is equal to $6 per day
    parking_allowance = days * PARKING_LIMIT

    # Ask user if they had any parking fees and how much it cost
    print('Did you have any parking fees on your trip?')
    fees = input('Enter y for yes or anything else for no: ')
    if fees == 'y' or fees == 'Y':
        parking_cost = float(input('Enter the total fees cost: '))
        # Prevents negative cost amounts
        while parking_cost < 0:
            print('Fee costs cannot be less than 0')
            parking_cost = float(input('Re-enter the total miles: '))
        # Tell the user if they were over or under the parking allowance
        if parking_cost > parking_allowance:
            print('You were over the parking allowance by $',
                  format(parking_cost - parking_allowance, '.2f'),
                  ' and will have to reimburse the company.', sep='')
        else:
            print('You were under the parking allowance by $',
                  format(parking_allowance - parking_cost, '.2f'), sep='')

    return parking_cost


def taxi_fees(days):
    # Default taxi fee cost is 0 so that it won't affect total cost
    # unless they answer yes to using a taxi and enter an amount
    taxi_cost = 0

    # Ask user if they any taxis and how much it cost and how many days
    print('Did you use any taxis on your trip?')
    taxi = input('Enter y for yes or anything else for no: ')
    if taxi == 'y' or taxi == 'Y':
        taxi_days = int(input('Enter the number of days you used a taxi: '))
        # Prevents negative amounts and taxi days cant be more or
        # less than total trip days
        while taxi_days < 0 or taxi_days > days:
            if taxi_days < 0:
                print('Days cannot be less than 0')
                taxi_days = int(input('Re-enter the number of days: '))
            elif taxi_days > days:
                print('Amount of days at taxi was used cannot be more' +
                      'than total days of the trip')
                taxi_days = int(input('Re-enter the number of days: '))
        taxi_cost = float(input('Enter the total cost of the taxis used: '))
        # Prevents negative amounts
        while taxi_cost < 0:
            print('Taxis costs cannot be less than 0')
            taxi_cost = float(input('Re-enter the total taxi cost: '))

        # Taxi allowance for trip is equal to $10 per day
        taxi_allowance = taxi_days * TAXI_LIMIT
        
        # Tell the user if they were over or under the taxi allowance
        if taxi_cost > taxi_allowance:
            print('You were over the taxi allowance by $',
                  format(taxi_cost - taxi_allowance, '.2f'),
                  ' and will have to reimburse the company.', sep='')
        else:
            print('You were under the taxi allowance by $',
                  format(taxi_allowance - taxi_cost, '.2f'), sep='')

    return taxi_cost
    

def registration_fees():
    # Default registration fee is 0 so that it won't affect total cost
    # unless they answer yes to having registration fees and enter an amount
    registration_cost = 0

    # Ask user if they had any registration fees and how much it cost
    print('Did you have any seminar or conference registration fees on your trip?')
    fees = input('Enter y for yes or anything else for no: ')
    if fees == 'y' or fees == 'Y':
        registration_cost = float(input('Enter the total of your registration fees: '))
        # Prevents negative cost amounts
        while registration_cost < 0:
            print('Registration fees cannot be less than 0')
            registration_cost = float(input('Re-enter the total registration fees: '))

    return registration_cost


def hotel_expenses(days):
    # Default hotel cost is 0 so that it won't affect total cost
    # until they enter an amount
    hotel_cost = 0

    # Hotel allowance for trip is equal to $90 per night
    hotel_allowance = (days - 1) * HOTEL_LIMIT

    # Ask user for the total hotel cost
    hotel_cost = float(input('Enter the total hotel cost: '))
    # Prevents negative cost amounts
    while hotel_cost < 0:
        print('Hotel costs cannot be less than 0')
        hotel_cost = float(input('Re-enter the hotel cost: '))
    
    
    if hotel_cost > hotel_allowance:
        print('You were over the hotel allowance by $',
              format(hotel_cost - hotel_allowance, '.2f'),
              ' and will have to reimburse the company.', sep='')
    else:
        print('You were under the hotel allowance by $',
              format(hotel_allowance - hotel_cost, '.2f'), sep='')

    return hotel_cost


def meal_expenses(days, depart, arrival, ampm_depart, ampm_arrive):
    # Variables for how many of each meal is allowed and totals for
    # amount spent on each breakfast, lunch, and dinner
    breakfast = days
    lunch = days
    dinner = days
    # Lists to hold the expenses of each type of meal
    breakfast_expense = [0] * days
    lunch_expense = [0] * days
    dinner_expense = [0] * days

    # Check departure times to see which meals are allowed on first day
    # and if they are ask for the amounts of each meal
    # Breakfast
    if (depart > 7 and
        (ampm_depart == 'am' or ampm_depart == 'a.m.')) or \
        (ampm_depart == 'pm' or ampm_depart =='p.m.'):
        breakfast -= 1
    elif depart < 7 and (ampm_depart == 'am' or ampm_depart == 'a.m.'):
        breakfast_expense[0] = float(input(
            'Enter the cost of your breakfast on day 1: '))
        # Prevents dollar amounts less than 0
        while breakfast_expense[0] < 0:
            print('Dollar amounts cannot be less than 0')
            breakfast_expense[0] = float(input(
                'Enter the cost of your breakfast on day 1: '))
    # Lunch
    if ampm_depart == 'pm' or ampm_depart == 'p.m.':
        lunch -= 1
    elif depart < 12 and (ampm_depart == 'am' or ampm_depart == 'a.m.'):
        lunch_expense[0] = float(input(
            'Enter the cost of your lunch on day 1: '))
        # Prevents dollar amounts less than 0
        while lunch_expense[0] < 0:
            print('Dollar amounts cannot be less than 0')
            lunch_expense[0] = float(input(
                'Enter the cost of your breakfast on day 1: '))
    # Dinner
    if depart > 6 and (ampm_depart == 'pm' or ampm_depart == 'p.m.'):
        dinner -= 1
    elif depart < 6 or (ampm_depart == 'am' or ampm_depart == 'a.m.'):
        dinner_expense[0] = float(input(
            'Enter the cost of your dinner on day 1: '))
        # Prevents dollar amounts less than 0
        while dinner_expense[0] < 0:
            print('Dollar amounts cannot be less than 0')
            dinner_expense[0] = float(input(
                'Enter the cost of your breakfast on day 1: '))
        
    # Get meal amounts for every day but the first and last
    for i in range(1, days - 1):
        print('Enter the cost of your breakfast on day ', i + 1, ': ',
              sep='', end='')
        breakfast_expense[i] = float(input())
        # Prevents dollar amounts less than 0
        while breakfast_expense[i] < 0:
            print('Dollar amounts cannot be less than 0')
            breakfast_expense[i] = float(input(
                'Re-enter the cost: '))
        print('Enter the cost of your lunch on day ', i + 1, ': '
              , sep='', end='')
        lunch_expense[i] = float(input())
        # Prevents dollar amounts less than 0
        while lunch_expense[i] < 0:
            print('Dollar amounts cannot be less than 0')
            lunch_expense[i] = float(input(
                'Re-enter the cost: '))
        print('Enter the cost of your dinner on day ', i + 1, ': ',
              sep='', end='')
        dinner_expense[i] = float(input())
        # Prevents dollar amounts less than 0
        while dinner_expense[i] < 0:
            print('Dollar amounts cannot be less than 0')
            dinner_expense[i] = float(input(
                'Re-enter the cost: '))
        
    # Check arrival times to see which meals are allowed on last day
    # and if they are ask for amounts of each meal
    # Breakfast
    if arrival < 8 and (ampm_arrive == 'am' or ampm_arrive == 'a.m.'):
        breakfast -= 1
    elif (arrival > 8 and
          (ampm_arrive == 'am' or ampm_arrive == 'a.m.')) or \
          (ampm_arrive == 'pm' or ampm_arrive == 'p.m.'):
        breakfast_expense[days - 1] = float(input(
            'Enter the cost of your breakfast on the last day: '))
        # Prevents dollar amounts less than 0
        while breakfast_expense[days - 1] < 0:
            print('Dollar amounts cannot be less than 0')
            breakfast_expense[days - 1] = float(input(
                'Re-enter the cost: '))
    # Lunch
    if (ampm_arrive == 'am' or ampm_arrive == 'a.m.') or (arrival >= 12 and
    (ampm_arrive == 'pm' or ampm_arrive == 'p.m.')) or (arrival <= 1 and
    (ampm_arrive == 'pm' or ampm_arrive == 'p.m.')):
        lunch -= 1
    elif arrival > 1 and (ampm_arrive == 'pm' or ampm_arrive == 'p.m.'):
        lunch_expense[days - 1] = float(input(
            'Enter the cost of your lunch on the last day: '))
        # Prevents dollar amounts less than 0
        while lunch_expense[days - 1] < 0:
            print('Dollar amounts cannot be less than 0')
            lunch_expense[days - 1] = float(input(
                'Re-enter the cost: '))
    # Dinner
    if arrival < 7:
        dinner -= 1
    elif arrival > 7 and (ampm_arrive == 'pm' and ampm_arrive == 'p.m.'):
        dinner_expense[days - 1] = float(input(
            'Enter the cost of your dinner on the last day: '))
        # Prevents dollar amounts less than 0
        while dinner_expense[days] < 0:
            print('Dollar amounts cannot be less than 0')
            dinner_expense[days - 1] = float(input(
                'Re-enter the cost: '))
    
    # Total meal expenses
    meal_expense = sum(breakfast_expense) + sum(lunch_expense) + sum(dinner_expense)
    
    # Calculate the meal allowance based on number of days and departure
    # and arrival times.
    break_allowance = breakfast * BREAKFAST_LIMIT
    lunch_allowance = lunch * LUNCH_LIMIT
    dinner_allowance = dinner * DINNER_LIMIT
    meal_allowance = break_allowance + lunch_allowance + dinner_allowance

    print('You were allowed $', format(meal_allowance, '.2f'), ' meal allowance', sep='')
    print('You spent $', format(meal_expense, '.2f'), sep='')
    
    if meal_expense > meal_allowance:
        print('You were over the meal allowance by $',
              format(meal_expense - meal_allowance, '.2f'),
              ' and will have to reimburse the company.', sep='')
        return meal_expense
    else:
        print('You were under the meal allowance by $',
              format(meal_allowance - meal_expense, '.2f'), sep='')
        return meal_expense
     

main()
