n = int(input("Enter number: "))
temp = n # temporary variable to set for checking the rev with this temp
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n //= 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")