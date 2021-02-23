total_cost, variable_cost, cost = map(int, input().split())
sales_vloume = 0
total_income = 0

if variable_cost >= cost:
    print(-1)

else:
    print(int(-(total_cost / (variable_cost - cost)) + 1))