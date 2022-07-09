numbers = list(range(1,10_001))
remove_numbers = []

for i in numbers :
    for j in str(i) :
        i += int(j)
    if i <= 10_000 :
        remove_numbers.append(i)
        
for i in set(remove_numbers) :
    numbers.remove(i)

for i in numbers :
    print(i)