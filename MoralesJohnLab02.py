# MoralesJohnLab02.py
# John Morales
# Class: CSCI 1411-00X
# Due Date: June 13, 2023
# This file converts the temperature in fahrenheit to celsius then calculates the temp
# 10 degrees after the given temperature


def main():
    # User will enter first and last name

    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")

    # Now the user will enter a temperature they would like to convert from F to C

    fahrenheit = eval(
        input(
            "What is the initial temperature in Fahrenheit that you would like to convert? "
        )
    )

    #Display the 
    
    print("Below is the conversion of", fahrenheit, "degrees plus the next 10 degrees")

    for i in range(11):
        celsius = ((fahrenheit + i) - 32) * (5 / 9)
        print(firstName, lastName, "Fahrenheit temperature:", fahrenheit + i, "is", celsius,
            "degrees in Celsius",)


main()
