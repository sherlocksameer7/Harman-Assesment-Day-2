starting_value = int(input("Enter the Starting value: "))
ending_value = int(input("Enter the Ending value: "))
print("The Prime Numbers are between: ")
for number in range(starting_value, ending_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)