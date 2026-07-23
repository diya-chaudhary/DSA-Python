def decode_string(s):
  stack=[]

  currentNumber=0
  currentString=""

  for ch in s:

    if ch.isdigit():
      currentNumber=currentNumber*10+int(ch)

    elif ch=="[":
      stack.append((currentNumber,currentString))
      currentNumber=0
      currentString=""

    elif ch=="]":
      number,previousString=stack.pop()
      currentString=previousString+number*currentString

    else:
      currentString+=ch

  return currentString

print(decode_string("3[a2[c]]"))

