def remove_k_digits(num,k):
  stack=[]

  for digit in num:
    while len(stack)>0 and stack[-1]>digit and k>0:
      stack.pop()
      k-=1
    
    stack.append(digit)

  while k>0:
    stack.pop()
    k-=1

  result="".join(stack)

  result=result.lstrip("0")

  if result=="":
    return "0"
  
  return result

print(remove_k_digits("1432219",3))