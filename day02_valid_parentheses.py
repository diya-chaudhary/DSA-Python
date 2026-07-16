def valid_parentheses(s):
  stack=[]
  pairs={')':'(',']':'[','}':'{'}
  for ch in s:
    if ch in "([{":
      stack.append(ch)
    else:
      if len(stack)==0:
        return False
      if stack[-1]!=pairs[ch]:
        return False
      else:
        stack.pop()
  return len(stack)==0
print(valid_parentheses("({})"))
print(valid_parentheses("([)]{)"))
      
