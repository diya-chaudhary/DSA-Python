def next_greater_circular(numbers):
  stack=[]
  n=len(numbers)
  result=[-1]*n

  for i in range(2*n-1,-1,-1):
    while len(stack)>0 and stack[-1]<=numbers[i%n]:
      stack.pop()

    if len(stack)>0:
      result[i%n]=stack[-1]

    stack.append(numbers[i%n])

  return result

print(next_greater_circular([1,2,1]))