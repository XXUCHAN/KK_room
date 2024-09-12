import sys

def my_round(x):
    if x - int(x) >= 0.5:
        return int(x)+1
    else:
        return int(x)
    
n = int(sys.stdin.readline().strip())
if n:
    level = []
    for _ in range(n):
        level.append(int(sys.stdin.readline().strip()))

    pivot = my_round(n*0.15)
    level.sort()
    if pivot > 0:
        print(my_round(sum(level[pivot:-pivot])/len(level[pivot:-pivot])))
    else:
        print(my_round(sum(level)/len(level)))
else:
    print(0)