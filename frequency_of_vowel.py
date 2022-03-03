string = input("Enter a sentence: ")
string = string.lower()
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
for same_index in vowels:  # same_index denotes the index of the given sentence to check in vowels of variables
    if same_index in string: # it is here for checking indexes of string variables
        vowels[same_index] = string.count(same_index)
print(vowels)