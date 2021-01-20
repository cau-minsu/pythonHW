start, stop = map(int, input().split())

i = start

while True:
    if i >= stop:
        break
    
    i += 1
    
    if i%10 == 3:
        continue   
    print(i, end=' ')