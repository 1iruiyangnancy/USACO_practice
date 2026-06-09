#题目来源：https://www.luogu.com.cn/problem/P1154

first_number_str = input("Please input the first number.")
last_number_str = input("Please input the last number.")
first_number = int(first_number_str)
last_number = int(last_number_str) + 1

number_of_number = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
for number in range(first_number, last_number):
    number_str = str(number)
    for idx in range(len(number_str)):
        number_of_number[number_str[idx]] += 1
for key, value in number_of_number.items():
    print(f'{key} {value}')
