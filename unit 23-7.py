row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
count = []
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if k < 0 or k > row-1 or l < 0 or l > col-1:
                        pass
                    elif matrix[k][l] == '*':
                        count.append('*')
            print(count.count('*'), end='')
            count.clear()
        elif matrix[i][j] == '*':
            print('*', end='')
    print()
            