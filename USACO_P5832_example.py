#题目来源：https://www.luogu.com.cn/problem/P5832

#输入部分：
#提示用户输入N，并判断N的值是不是在允许的范围内，如果不在允许的范围内，则提示错误，并让用户重新输入。
n = 0
while n < 1 or n > 100:
    n_str = input(f'请输入农场数量N(1<= N <=100):')
    n = int(n_str)
    if n < 1 or n > 100:
        print(f'农场数量N的值{n}不在允许的范围(1<= N <=100)内，请重新输入。')

#提示用户输入农场邮箱颜色顺序字符串，并判断字符串长度和N的值是不是相等，如果不相等，则提示错误，并让用户重新输入。
mailbox_str = ''
mailbox_len = -1
while mailbox_len != n:
    mailbox_str = input("请输入农场邮箱颜色顺序的字符串：")
    mailbox_len = len(mailbox_str)
    if mailbox_len != n:
        print(f'农场邮箱颜色顺序字符串的长度{mailbox_len}不等于农场数量{n}，请重新输入。')

#把输入的字符串转换为全部大写，规范化输入的字符串，方便后续计算。
mailbox_str = mailbox_str.upper()

print(f'输入的农场数量N={n},农场邮箱颜色字符串是{mailbox_str}')

#子串长度从1开始，到字符串长度-1结束，依次按不同的长度取子串进行对比
for sub_str_len in range(1, mailbox_len - 1):
    #声明一个boolean变量，记录有没有相同颜色的子串，初始化值为假(False)
    has_same_color = False
    #从第一个字符开始，依次取子串和子串后的字符串
    for idx in range(0, mailbox_len):
        #取子串
        sub_str = mailbox_str[idx : idx + sub_str_len]
        #取子串后的字符串
        remain_str = mailbox_str[idx + sub_str_len : mailbox_len]
        #如果剩余的字符串中包含子串
        if(sub_str in remain_str):
            #设置有相同颜色子串的变量
            has_same_color = True
            #退出子串比较的循环，按下一个长度再开始比较
            break
    #比较循环结束后，如果没有相同的子串，说明找到了没有重复颜色子串的长度，打印输出。
    if(not has_same_color):
        print(f'最小的长度为{sub_str_len}时，没有相同颜色的连续邮箱')
        break




