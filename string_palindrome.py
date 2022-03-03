string = input(("Enter any word: "))
# string.lower()
if string.lower() == string.lower()[::-1]:  #string slicing operator has been used for reverse it using [::-1]
      print("The string is a palindrome")
else:
      print("The string is not a palindrome")