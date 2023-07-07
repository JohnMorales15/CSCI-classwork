# John
# Morales
# Date: June 21, 2023


def main():
    userStr = input("Please enter a string: ")
    userNum = int(input("Please enter a single number: "))

    # Each character in userStr will be converted to ASCII number and userNum will be added to the number
    encodedStr = ""
    for ch in userStr:
        encodedStr += chr(ord(ch) + userNum)

    print("Your Encoded message is: ", encodedStr)

    decodedStr = ""
    for i in encodedStr:
        decodedStr += chr(ord(i) - userNum)

    print("Your Decoded message is: ", decodedStr)


main()
