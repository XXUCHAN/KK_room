n,k = input().split()

term = list(i+1 for i in range(int(n)))

que = list()
result = list()
start = int(k) - 1
for i in range(int(n)):
    result.append(term.pop(start))
    if len(term) == 0:
        break
    start = (start + int(k)- 1 ) % len(term)

print('<',end="")
print(*result,sep=', ',end="")
print('>')
