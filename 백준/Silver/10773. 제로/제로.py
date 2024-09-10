n = int(input())
order = [ list(map(int,input().split())) for _ in range(n) ]

result = list()

for i in range(n):

    if order[i][0] == 0:
        result.pop(len(result) -1 )
    else:
        result.append(order[i][0])
print(sum(result))