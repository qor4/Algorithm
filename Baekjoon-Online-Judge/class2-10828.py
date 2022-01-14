import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    imp = input().strip()
    if imp[:2] == 'pu':
        imp, num = imp.split()
        stack.append(int(num))
    elif imp[:2] == 'po':
        print(stack.pop()) if stack else print(-1)
    elif imp[:2] == 'si':
        print(len(stack))
    elif imp[:2] == 'em':
        print(0) if stack else print(1)
    elif imp[:2] == 'to':
        print(stack[-1]) if stack else print(-1)
