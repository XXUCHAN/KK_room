n = int(input())
parenthesis = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    stack = list()
    for j in range(len(parenthesis[i])):
        stack.append(parenthesis[i][j])
        if parenthesis[i][j] == ')':
            if '(' in stack:
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')