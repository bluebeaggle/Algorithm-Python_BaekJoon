list_dice = list(map(int, input().split()))

if len(set(list_dice)) == 1 :
    print(list_dice[0]*1000+10000)
elif len(set(list_dice)) == 3:
    print(max(list(list_dice))*100)
else :
    print(1000 + (sum(list_dice)-sum(list(set(list_dice))))*100)