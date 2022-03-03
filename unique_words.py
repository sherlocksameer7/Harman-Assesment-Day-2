string = input("Enter a sentence: ")
print("The words in that sentence are: ", string.split())
unique_words = set(string)
print("The unique words in the sentence: ", unique_words)