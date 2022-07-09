n = int(input())

for i in range(n) :
  ox = list(input())
    
  Sum = 0
  Count = 1
    
  for j in ox :
    if j == 'O' :
      Sum += Count
      Count += 1
    else :
      Count = 1
  print(Sum)