def next_greater(numbers):
  stack=[]
  result=[]
  for i in range(len(numbers)-1,-1,-1):
    while len(stack)>0 and stack[-1]<=numbers[i]:
      stack.pop()
      if len(stack)==0:
        result.append(-1)
      else:
        result.append(stack[-1])

      
