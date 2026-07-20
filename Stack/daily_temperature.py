def daily_temperature(temperatures):
  result=[]
  stack=[]
  for i in range(len(temperatures)-1,-1,-1):

    while len(stack)>0 and temperatures[stack[-1]]<=temperatures[i]:
      stack.pop()

    if len(stack)==0:
      result.append(0)
    else:
      result.append(stack[-1]-i)

    stack.append(i)
  
  result.reverse()

  return result

print(daily_temperature([73,74,75,71,69,72,76,73]))

