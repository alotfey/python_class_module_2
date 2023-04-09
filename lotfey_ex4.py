##########################################
# CS 1110A - Programming in Python       #
# Module 2 - Exercise 4 - Drunken Pirate #
# Author: Ahmed Lotfey                   #
# Date:   03/25/2023                     #
##########################################

# calculate function definition
def calculate(data):
    # prints each of the numbers on a single line separated with spaces.
    print("1:", end=" ")
    for num in data:
        print(num, end=" ")
    print("\n")
    # prints each number and its square on a new line.
    print("2: n   n^2")
    for num in data:
        print(f"{num: >4}{num ** 2 : > 6}")
    total_values = sum(data)
    print()
    # prints the total of the numbers.
    print(f"3: The total of the values is {total_values} \n")
    # prints the product of the numbers.
    product = 1
    for num in data:
        product *= num
    print(f"4: The prodcut of the values is {format(product, ',')}")

# main function
def main():
    print("Using loops\n")
    data1 = [20, 15, 40, 17, 10, 30, 11, 18, 45, 10, 20, 88]
    data2 = [21, 8, 10, 18, 30, 10, 1, 20, 18, 19, 10]

    print("Calculations for data1:\n")
    # call calculate function for data1
    calculate(data1)

    print("\nCalculations for data2:\n")
    # call calculate function for data2
    calculate(data2)
    print("\nDone!\n")

# call main function
if __name__ == "__main__":
    main()
