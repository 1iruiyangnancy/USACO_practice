#题目来源：https://www.luogu.com.cn/problem/P1201

n = 0
while n<1 or n>10:
    n_str = input(f'Please input {n} (1<= N <=10):')
    n = int(n_str)
    if n < 1 or n > 10:
        print(f'The value of {n} is not in the given range (1<= N <=10), please input again.')
n = int(n_str)
friends = []
for idx in range(n):
    name = input('Please input the name of the friend :')
    friends.append(name.lower())

#送出礼物人的名字数组
give_gifts_person_names = []

#原有的钱的数目，使用字典保存
original_amount_of_money = {}

#将收到这个人礼物的人的个数，使用字典保存
receive_gifts_person_number = {}

#收礼人的名字数组，使用字典保存，key为名字，第二维为收礼人的名字数组
receive_gifts_person_names = {}

for i in range(n):
    gg_name = input('Please input the name of the give gifts person :')
    give_gifts_person_names.append(gg_name.lower())
    gg_m_p_input = input("Please enter the original amount of money and the number of people who will receive this person's gift, separated by a space. :")
    gg_m_p = gg_m_p_input.split(' ')
    original_amount_of_money[gg_name] = int(gg_m_p[0])
    receive_gifts_person_number[gg_name] = int(gg_m_p[1])
    #每个送出礼物人所对应的收到礼物的人的姓名数组
    rg_names_row = []
    for j in range(receive_gifts_person_number[gg_name]):
        rg_name = input(f'Please enter the name of the No. {j + 1} person to receive a gift:')
        rg_names_row.append(rg_name.lower())
    #把每个送出礼物人所对应的收到礼物的人的姓名数组加入到二维数组中
    receive_gifts_person_names[gg_name] = rg_names_row

#计算每个朋友收到的钱，用字典存放名字和收到钱的对应关系，利用字段的key/value属性快速根据名字找到收到的钱数
rev_money = {}

for i in range(n):
    for j in range(receive_gifts_person_number[friends[i]]):
        if receive_gifts_person_names[friends[i]][j] in rev_money:
            rev_money[receive_gifts_person_names[friends[i]][j]] += original_amount_of_money[friends[i]] / len(receive_gifts_person_names[friends[i]])
        else:
            rev_money[receive_gifts_person_names[friends[i]][j]] = original_amount_of_money[friends[i]] / len(receive_gifts_person_names[friends[i]])

for i in range(n):
    print(f'{friends[i]} {rev_money[friends[i]] - original_amount_of_money[friends[i]]}')


