# John
# Morales
# Date: June 27, 2023
# Description: This program will find the average quiz scores for students
import math


def main():
    infileName = input("Please enter the name of the input file: ")
    infile = open(infileName, "r")

    outfileName = input("Please enter the name of the output file: ")

    outfile = open(outfileName, "w")

    # iterate through each line in the input file
    for line in infile:
        # splitting the lines into a list
        student = line.split()
        name = student[0]
        # iterating through each index starting at the numbers [1]

        sumOfNums = 0
        for i in range(1, len(student)):
            sumOfNums += int(student[i])

        avg = sumOfNums / (len(student) - 1)
        print(name, avg)
        print(name, avg, file=outfile)

    infile.close()
    outfile.close()
