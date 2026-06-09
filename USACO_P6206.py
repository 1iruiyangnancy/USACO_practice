#题目来源：https://www.luogu.com.cn/problem/P2606

N = 0
while N < 1 or N > 1000000:
    N_str = input("Please input Bessie's number (1<= N <=1000000):")
    N = int(N_str)
    if N < 1 or N > 1000000:
        print(f'The value of {N} is not in the given range (1<= N <=1000000), please input again.')

score = 0
while N != 1:
    if N % 2 == 1:
        N = N * 3 + 1
    else:
        N = N / 2
    score += 1
print(score)