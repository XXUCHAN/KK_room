n = int(input())
order = [ list(input().split()) for _ in range(n) ]

result = list()

for i in range(n):
    if order[i][0] == "push":
        result.append(order[i][1])
    elif order[i][0] == "front":
        if len(result) == 0 :
            print("-1")
        else:
            print(result[0])
    elif order[i][0] == "back":
        if len(result) == 0 :
            print("-1")
        else:
            print(result[-1])
    elif order[i][0] == "size":
        print(len(result))
    elif order[i][0] == "empty":
        if len(result) == 0 :
            print("1")
        else:
            print("0")
    elif order[i][0] == "pop":
        if len(result) == 0:
            print("-1")
        else:
            print(result.pop(0))
