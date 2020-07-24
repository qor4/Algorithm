A = int(input())
B = int(input())

num3 = (B % 10) * A
num4 = (B % 100) // 10 * A
num5 = (B // 100) * A
num6 = A * B
print(num3)
print(num4)
print(num5)
print(num6)