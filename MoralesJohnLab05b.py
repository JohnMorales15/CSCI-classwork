# John Morales
# Date: June 20th, 2023


def main():
    firstName = input("Enter you first name: ")
    lastName = input("Enter your last name: ")

    userName = lastName + firstName[0]
    print("Thank you! Your username is: " + userName.lower())

    emailAddress = firstName + "." + lastName + "@ucdenver.edu"
    print("Your email address is: " + emailAddress.lower())


main()
