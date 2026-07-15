def two_sum(numbers,target):
  seen={}
  
  for i in range(len(numbers)):
    complement=target-numbers[i]
   
    if complement in seen:
      return[seen[complment],i]
   
    seen[numbers[i]]=i

print(two_sum([2,7,11,15],9))
