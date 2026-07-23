def trap(height):
  stack=[]
  water=0

  for i in range(len(height)):

     while len(stack)>0 and height[stack[-1]]<height[i]:
        bottom=stack.pop()

        if len(stack)==0:
           break
        
        left=stack[-1]

        distance=i-left-1

        bounded_height=min(height[left],height[i])-height[bottom]
         
        water=water+distance*bounded_height
      
     stack.append(i)
  
  return water

print(trap([3,0,2]))