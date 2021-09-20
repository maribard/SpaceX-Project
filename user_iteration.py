def user_iteration():
    a = user_iteration1()
    b = user_iteration2()
    c = user_iteration3()

    return a, b ,c


def user_iteration1():
    choice1 = 'wrong'
    
    acceptable_range = range(1, 70)
    within_range = False


    # Two condition to check
    # Digit or within_range == False
    while choice1.isdigit() == False or within_range == False:

        choice1 = input("Enter number of most reused rocket cores to fetch (1-69): ")

        # Digit check
        if choice1.isdigit() == False:
            print("Sorry that is not digit!")

        # Range check
        if choice1.isdigit() == True:
            if int(choice1) in acceptable_range:
                within_range = True
            else:
                print("Sorry, you are out of acceptable range (1-69)")

    number_of_cores = int(choice1)
    return number_of_cores





def user_iteration2():
    choice2 = 'wrong'


    while choice2 not in ['Y', 'N']:

        choice2 = input("Include or exclude unsuccessful flights? (Y or N): ")

        if choice2 not in ['Y', 'N']:
            print("Sorry, I dont understand, please choice Y or N")


    unsuccessful_flights = choice2
    return unsuccessful_flights







def user_iteration3():
    choice3 = 'wrong'


    while choice3 not in ['Y', 'N']:

        choice3 = input("Include or exclude planned future missions? (Y or N): ")

        if choice3 not in ['Y', 'N']:
            print("Sorry, I dont understand, please choice Y or N")

    future_missions = choice3

    return(future_missions)
