def largest_rectangle(heights):

  stack=[]
  psi=[]

  for i in range(len(heights)):

    while len(stack)>0 and heights[stack[-1]]>=heights[i]:
      stack.pop()

    if len(stack)==0:
      psi.append(-1)

    else:
      psi.append(stack[-1])

    stack.append(i)

    # find next smaller elements

  stack=[]
  nsi=[]

  for i in range(len(heights)-1,-1,-1):

    while len(stack)>0 and heights[stack[-1]]>=heights[i]:
      stack.pop()

    if len(stack)==0:
      nsi.append(len(heights))

    else:
      nsi.append(stack[-1])

    stack.append(i)

  nsi.reverse()

 # Find area

  max_area=0
  
  for i in range(len(heights)):
    
    width=nsi[i]-psi[i]-1
    area=heights[i]*width

    if area>max_area:
      max_area=area

  return max_area

print(largest_rectangle([2,1,5,6,2,3]))



  

    
