print("Enter any sentence: ")
text = input()
text = text.split()
bigWordLen = 0

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen > bigWordLen:
    bigWordLen = wrdLen

print("Largest Word: ")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen == bigWordLen:
    print(wrd)