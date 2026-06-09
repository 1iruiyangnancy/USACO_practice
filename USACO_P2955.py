#题目来源：https://www.luogu.com.cn/problem/P2955

amount_of_number_str = input("Please input the amount of number.")
amount_of_number = int(amount_of_number_str)
number = []
for idx in range(amount_of_number):
    number_str = input(f"Please input number {idx} :")
    number.append(int(number_str))

for value in number:
    if value % 2 == 0:
        print("even")
    else:
        print("odd")
