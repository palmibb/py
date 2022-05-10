buyer1=input()
buyer2=input()
urna=input() 
sum1=0
sum2=0
for j in urna:
  if j in buyer1:
    sum1+=1
  if j in buyer2:
    sum2+=1
  if sum1>sum2:
    print("A",end="")
  elif sum2>sum1:
    print("B",end="")
  else:
    print("E",end="")