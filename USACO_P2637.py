#题目来源：https://www.luogu.com.cn/problem/P2637

num_of_forage_and_farmer_str = input("Please input the number of forage, blank, the number of farmer.")
numbers = num_of_forage_and_farmer_str.split()
num_of_forage = int(numbers[0])
num_of_farmer = int(numbers[1]) 
p = []
for idx in range(num_of_farmer):
    p_str = input(f"Please input farmer {idx + 1} price :")
    p.append(int(p_str))


money_max = 0
p_max = 0
for value in p:
    money = 0
    for value_1 in p:
        if value_1 >= value:
           money += value
    if money >= money_max:
        money_max = money
        p_max = value
print(f"FJ can get {money_max} at price of {p_max}.")