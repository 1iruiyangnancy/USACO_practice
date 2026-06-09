N = 0
while N < 1 or N > 100:
    N_str = input(f'Please input {N} (1<= N <=100):')
    N = int(N_str)
    if N < 1 or N > 100:
        print(f'The value of {N} is not in the given range (1<= N <=100), please input again.')
color_str = ''
color_len = -1
while color_len != N:
    color_str = input("Please input color :")
    color_len = len(color_str)
    if color_len != N:
        print(f'The length of the string {color_len}is not equal to {N}, please input again.')
color_str = color_str.upper()

