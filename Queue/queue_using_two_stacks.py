stack1=[]
stack2=[]

def enqueue(x):
  stack1.append(x)

def dequeue():

  if len(stack2)==0:

    while len(stack1)>0:
      x=stack1.pop()
      stack2.append(x)

  return stack2.pop()

enqueue(10)
enqueue(20)
enqueue(30)

print(dequeue())   
print(dequeue())   

enqueue(40)

print(dequeue())   
print(dequeue())   
