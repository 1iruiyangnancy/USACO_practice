#题目来源：https://www.luogu.com.cn/problem/P1200

comet_name = input("Please input comet name.")
group_name = input("Please input group name.")
comet_name = comet_name.upper()
group_name = group_name.upper()

letters_to_numbers = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
result_comet_name = 1
result_group_name = 1
for idx in range(len(comet_name)):
    result_comet_name *= letters_to_numbers[comet_name[idx]]
remainder_comet_name = result_comet_name % 47
for idx in range(len(group_name)):
    result_group_name *= letters_to_numbers[group_name[idx]]
remainder_group_name = result_group_name % 47
if remainder_comet_name == remainder_group_name:
    print("GO")
else:
    print("STAY")