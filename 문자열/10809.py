String = input().upper()
Count = {}

for i in String :
    try : Count[i] += 1
    except : Count[i] = 1

max_value = [k for k,v in Count.items() if max(Count.values())== v]
if len(max_value) >=2 :
  print('?')
else :
  print(max_value[0])