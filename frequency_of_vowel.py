string = input("Enter a sentence: ")
string = string.lower()
vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}  # it means a dictionary to initialise the value
for i in vowels:  # same_index denotes the index of the given sentence to check in vowels of variables
    if i in string: # it is here for checking indexes of string variables
        vowels[i] = string.count(i)  # count it
print(vowels)