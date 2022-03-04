print("Enter any sentence: ")
text = input()
text = text.split()
smallestword = 0

for word in text:
  wordLen = len(word)
  if wordLen < smallestword:
    smallestword = wordLen

print("Smallest Word: ")
for word in text:
  wordLen = len(word)
  if wordLen == smallestword:
    print(word)