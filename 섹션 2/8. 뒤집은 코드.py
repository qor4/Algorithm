n = int(input())

num_list = list(map(str, input().split()))

def reverse(x):
    count = 0
    x = ''.join(reversed(x))
    for j in range(len(x)):
        if x[j] == '0':
            count += 1
        else:
            break
    x = x[count:]
    return x

def isPrime(x):
    if int(x) != 1:
        for k in range(2, int(x)):
            if int(x) % k == 0:
                break
        else:
            print(x, end=" ")



for i in range(len(num_list)):
    num_list[i] = reverse(num_list[i])
    isPrime(num_list[i])