print("Enter any sentence: ")
text = input()
text = text.split()
smallWordLen = 0

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen < smallWordLen:
    smallWordLen = wrdLen

print("Smallest Word: ")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen == smallWordLen:
    print(wrd)