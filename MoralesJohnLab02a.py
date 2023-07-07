#Fie MoralesJohnLab02a.py
#This is lab 2. It takes in a temperature in Fahrenheit and converts it to Celsius.
#It also queries the user for their name

def main():
    # first, ask the user for their first and last names
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    # no ask them fo rthe temperatrue they wish to convert
    fahren = (int)(input("What is the temperature in Fahrenheit? "))

    # next we conver using the standard F to C formula
    celsius = (fahren - 32)*(5/9)

    # finally, print out eh conversion

    print(firstName, lastName, "the Celsius temperature is ", celsius, "degrees")

main()
