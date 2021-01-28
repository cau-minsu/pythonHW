a = input().split(';')
a = list(map(int, a))
a.sort(reverse=True)
print(a)
for i in range(len(a)-1):
    print('{0:>9,}'.format(a[i]))
    