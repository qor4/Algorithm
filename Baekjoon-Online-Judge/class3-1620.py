import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemons_num = {}
pokemons_name = {}

for i in range(n):
    name = input().strip()
    pokemons_name[name] = i + 1
    pokemons_num[i + 1] = name

for _ in range(m):
    ask = input().strip()
    if ask.isdigit():
        print(pokemons_num[int(ask)])
    else:
        print(pokemons_name[ask])