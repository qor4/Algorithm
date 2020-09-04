up, down, height = map(int, input().split())
if height <= up:
    print(1)
elif height % (up - down) == 0:
    if height % (up - down) + down <= up:
        print((height // (up - down)) - 1)
    else:
        print(height // (up - down))
elif height % (up - down) != 0:
    if height % (up - down) <= up:
        print(height // (up - down) + 1)