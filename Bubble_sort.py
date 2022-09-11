a = [3, 2, 1]
swap = 0


for i in range(len(a)-1):

    for x in range(0, len(a)-i-1):
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]
            swap += 1

print('Array is sorted in ' + str(swap) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))
