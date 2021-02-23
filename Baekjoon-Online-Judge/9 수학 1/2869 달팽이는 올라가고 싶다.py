up, down, height = map(int, input().split())
day = (height - up) // (up - down)
if height <= up:
    print(1)
elif (height - up) % (up - down) == 0:
    print(day + 1)
elif (height - up) % (up - down) != 0:
    print(day + 2)
