#题目来源：https://www.luogu.com.cn/problem/P1202

n = 0
while n < 1 or n > 400:
    n_str = input('Please input the number of years from 1900 (1<= n <=400):')
    n = int(n_str)
    if n < 1 or n > 400:
        print(f'The value of {n} is not in the given range (1<= n <=400), please input again.')
n = int(n_str)

number_of_days = {6:0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0}
day_of_week = 0
for year in range(1900, 1900 + n):
    for month in range(1, 13):
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29
            else:
                days = 28
        elif month in (4, 6, 9, 11):
            days = 30
        else:
            days = 31
        for day in range(1,days + 1):
            day_of_week = (day_of_week + 1) % 7
            if day == 13:
                number_of_days[day_of_week] += 1
print(f'{number_of_days[6]} {number_of_days[0]} {number_of_days[1]} {number_of_days[2]} {number_of_days[3]} {number_of_days[4]} {number_of_days[5]}')