n = int(input())

while(n != 1):
    if n == 2:
        print(n)
        break
    for i in range(2, n):
        if(n % i == 0):
            n = int(n / i)
            print(i)
            break
    if i == n - 1:
        print(n)
        break
