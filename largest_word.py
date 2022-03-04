print("Enter any sentence: ")
text = input()
text = text.split()
bigWordLen = 0

for word in text:
  wordlen = len(word)
  if wordlen > biggestword:
    biggestword = wordlen

print("Largest Word: ")
for word in text:
  wordlen = len(word)
  if wordlen == biggestword:
    print(word)