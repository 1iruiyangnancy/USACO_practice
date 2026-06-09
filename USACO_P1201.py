n = 0
while n < 1 or n > 10:
    n_str = input(f'Please input {n} (1<= N <=10):')
    n = int(n_str)
    if n < 1 or n > 10:
        print(f'The value of {n} is not in the given range (1<= N <=10), please input again.')
n = int(n_str)
friends = []
for idx in range(n):
    name = input('Please input the name of the friend :')
    friends.append(name.lower())
for idx in range(n):
    name_give_gift = input('Please input the friend who gives the gift :')
    money_and_people = input('Please input the money, blank, the number of people who recieves the gift:')
    numbers = money_and_people.split()
    money = int(numbers[0])
    people = int(numbers[1])
    for idx in range(people):
        friends_recieve = input(f'Please input friend {idx} who recieves gift :')
