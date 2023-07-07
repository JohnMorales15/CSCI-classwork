# John
# Morales
# Date: June 28, 2023
# Description: This programs finds the doubles of a given list


def findDoubles(list):
    doubles = []
    for i in range(len(list)):
        nums = list[i] * 2
        doubles.append(nums)
    return doubles


def main():
    nums = []
    for i in range(5):
        num = eval(input("Please enter numbers: "))
        nums.append(num)
    result = findDoubles(nums)

    print(result)
