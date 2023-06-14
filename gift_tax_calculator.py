def taxCalculator():

    print()
    print(
        'Finnish gift tax calculator. Give amount of the gift and the program calculates amount of the tax. ("-1" ends the program)\n'
    )

    while True:

        gift = input("Amount of the gift? ")

        try:
            gift = float(gift) #accepts only numbers

            if gift == -1.0: #ends the program
                print("Thank you for using this program!")
                break

            taxcalculator = { #dictionary for tax calculation
                ((gift - 1), 5000): 0,
                (5000, 25000): (100 + (gift - 5000) * 0.08),
                (25000, 55000): (1700 + (gift - 25000) * 0.10),
                (55000, 200000): (4700 + (gift - 55000) * 0.12),
                (200000, 1000000): (22100 + (gift - 200000) * 0.15),
                (1000000, (gift + 1)): (142100 + (gift - 1000000) * 0.17),
            }

            for (lower_limit, upper_limit), tax in taxcalculator.items(): #calculates the tax
                if lower_limit <= float(gift) < upper_limit:
                    print(
                        f'Amount of the tax: {str(round(tax, 2)) + " euros" if tax > 0 else "No taxation!"}'
                        + "\n"
                    )

        except ValueError: #if input is not a number
            print("Give number!\n")


if __name__ == "__main__": # main function that runs the program

    taxCalculator()
