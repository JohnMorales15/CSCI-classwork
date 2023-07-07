# John
# Morales
# Date: July 5, 2023
# Description: This program will take a data file and create an output file using functions
import math

##############################################################
# Function Name: read_data
# Description: Reads a set of numbers from an input file.
# Parameter: file_name - name of the input file
# Returns list of numbers
##############################################################


def read_data(file_name):
    infile = open(file_name, "r")
    nums = infile.readlines()
    list_of_numbers = [eval(n) for n in nums]
    # print(list_of_numbers)
    infile.close()
    return list_of_numbers


##############################################################
# Function Name: compute_sum
# Description: Calculates the sum of a list of numbers
# Parameter: list of numbers
# Returns the sum of the list of numbers
##############################################################


def compute_sum(my_list):
    sum = 0
    for num in my_list:
        sum += num

    return sum


##############################################################
# Function Name: compute_mean
# Description: Calculates the mean of a list of numbers
# Parameter: list of numbers
# Returns the mean of the list of numbers
##############################################################


def compute_mean(my_list):
    result = compute_sum(my_list) / len(my_list)

    return result


#############################################################
# Function Name: compute_sd
# Description: Calculates the standard deviation of a list of numbers
# Parameter: list of numbers
# Returns the standard deviation of the list of numbers
##############################################################


def compute_sd(my_list):
    mean = compute_mean(my_list)
    sum = 0
    for num in my_list:
        deviation = num - mean
        sqDeviation = deviation**2
        sum += sqDeviation
    size = len(my_list)
    result = sum / (size - 1)
    sd = math.sqrt(result)

    return sd


#############################################################
# Function Name: write_result
# Description: Writes the result of the sum, mean and sd functions
# Parameter: output file, sum, means and sd
# Creates an output file with the sum, mean and sd
##############################################################


def write_result(outputFilename, sum, mean, sd):
    outputFile = open(outputFilename, "w")

    print("Sum is:", float("{:.2f}".format(sum)))
    print("Sum is:", float("{:.2f}".format(sum)), file=outputFile)
    print("Mean is:", float("{:.2f}".format(mean)))
    print("Mean is:", float("{:.2f}".format(mean)), file=outputFile)
    print("Standard Deviation is:", float("{:.2f}".format(sd)))
    print("Standard Deviation is:", float("{:.2f}".format(sd)), file=outputFile)

    outputFile.close()


def main():
    infile = input("Please enter file name that you would like to use: ")
    outfile = input("Please enter file name that you would like to create: ")
    my_list = read_data(infile)
    sum = float("{:.2f}".format(compute_sum(my_list)))
    mean = float("{:.2f}".format(compute_mean(my_list)))
    sd = float("{:.2f}".format(compute_sd(my_list)))
    write_result(outfile, sum, mean, sd)
