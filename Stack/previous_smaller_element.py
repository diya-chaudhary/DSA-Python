def previous_smaller(numbers):
  result=[]
  stack=[]
  for i in range(len(numbers)):
    while len(stack)>0 and stack[-1]>=numbers[i]:
      stack.pop()
    if len(stack)==0:
      result.append(-1)
    else:
      result.append(stack[-1])
    stack.append(numbers[i])
  return result
print(previous_smaller([4,6,1,5]))
