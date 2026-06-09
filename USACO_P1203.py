#题目来源：https://www.luogu.com.cn/problem/P1203

n = 0
while n < 3 or n > 350:
    n_str = input('Please input number of beads (3<= n <=350):')
    n = int(n_str)
    if n < 3 or n > 350:
        print(f'{n} is not in the given range (3<= n <=350), please input again.')
n = int(n_str)
color_str = ''
color_len = -1
while color_len != n:
    color_str = input("Please input color of necklace:")
    color_len = len(color_str)
    if color_len != n:
        print(f'The length of the string {color_len} is not equal to {n}, please input again.')
color_str = color_str.lower()

color_str_1 = color_str + color_str + color_str
bead_max = 0
for idx in range(n , n * 2):
    if color_str_1[idx] != color_str_1[idx + 1]:
        break_position = idx
        idx_pre = idx
        bead = 2
        while color_str_1[break_position] == color_str_1[idx_pre - 1] or color_str_1[idx_pre - 1] == 'w':
           idx_pre -= 1
           bead += 1
        idx_next = idx + 1
        while color_str_1[break_position + 1] == color_str_1[idx_next + 1] or color_str_1[idx_next + 1] == 'w':
            idx_next += 1
            bead += 1
        if bead > bead_max:
            bead_max = bead
print(bead_max)