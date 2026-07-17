# Next Greater Element 
# Approach 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def next_greater(nums):
  result=[]
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[j]>nums[i]:
        result.append(nums[j])
        break
    else:
      result.append(-1)
  return result
print(next_greater([3,6,2,8,9,1]))


# Approach 2: Stack
# Time Complexity: O(1)
# Space Complexity: O(n) 

def next_greater(nums):
  result=[]
  stack=[]
  for i in range(len(nums)-1,-1,-1):
    while len(stack)>0 and stack[-1]<=nums[i]:
      stack.pop()
    if len(stack)==0:
      result.append(-1)
    else:
      result.append(stack[-1])
    stack.append(nums[i])
  result.reverse()
  return result
print(next_greater([3,6,2,8,9,1]))