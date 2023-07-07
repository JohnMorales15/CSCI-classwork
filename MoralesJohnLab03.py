def main():
    length = eval(input("Enter the length of the box in inches: "))
    width = eval(input("Enter the width of the box in inches: "))
    perimeter = (2 * width) + (2 * length)

    print("Thank you, it appears your box has a perimeter of", perimeter, "inches")

    trimBoard = round(perimeter / 12)
    print("You will need to buy", trimBoard, "trim boards")

    totalCost = round(trimBoard * 1.88, 2)
    print("This will cost $", totalCost)

    wasteTrim = round((trimBoard * 12) - perimeter, 2)

    wasteCost = round(wasteTrim * (1.88 / 12), 2)

    print(
        "You will waste",
        wasteTrim,
        "inches of trim, which equates to a waste of $",
        wasteCost,
    )


main()
