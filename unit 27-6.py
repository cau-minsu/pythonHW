with open('words.txt', 'r') as file:
    lists = list(file.read().split())
    for i in range(len(lists)):
        if 'c' in lists[i]:
            print(lists[i].strip(',.'))
        else:
            pass