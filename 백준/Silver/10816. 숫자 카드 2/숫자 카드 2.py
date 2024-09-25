import sys

n = int(sys.stdin.readline())
term = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
hand = list(map(int, sys.stdin.readline().split()))


term.sort()


def find_left(item):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if term[mid] < item:
            start = mid + 1
        else:
            end = mid - 1
    return start


def find_right(item):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if term[mid] <= item:
            start = mid + 1
        else:
            end = mid - 1
    return start


def count_occurrences(item):
    left = find_left(item)   
    right = find_right(item)  
    return right - left        


for i in hand:
    print(count_occurrences(i), end=" ")
