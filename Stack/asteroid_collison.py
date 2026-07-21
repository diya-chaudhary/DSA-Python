def asteroid_collison(asteroids):
  stack=[]

  for asteroid in asteroids:

    alive=True
    
    while len(stack)>0 and stack[-1]>0 and asteroid<0:

      if abs(stack[-1])>abs(asteroid):
        alive=False
        break

      elif abs(stack[-1]<abs(asteroid)):
        stack.pop()
      
      else:
        stack.pop()
        alive=False
        break

    if alive:
      stack.append(asteroid)

  return stack

print(asteroid_collison([8,-8]))
print(asteroid_collison([10,2,-5]))
print(asteroid_collison([-2,-1,1,2]))
print(asteroid_collison([1,-2,-2,-2]))

