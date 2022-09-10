i = int(input())
list = []
for a in range(i):
    x = int(input())
    list.append(x)

for x in list:
    if x + 3 > 40:
        if x % 5 == 0:
            print(x)
        elif x % 5 == 3:
            print(x+2)
        elif x % 5 == 4:
            print(x+1)
        else:
            print(x)
    else:
        print(x)
