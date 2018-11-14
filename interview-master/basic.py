# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出

str_list = []
for i in s:
    str_list.append(i)
str_list.sort()
for item in str_list:
    print(item, end=' ')
print('\n****************')
# 问题二：数值比较

n = [9, 15, 23, 89, 33, 26, 2, 76]

# 请编写代码，找出数组中的最大数与最小数

max_num = max(n)
min_num = min(n)
print('max_num = %s, min_num = %s' % (max_num, min_num))
print('****************')

# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子

str_list = a.split(',')
name = input('name: ')
address = input('address: ')
str_list[3] = name
str_list[5] = address
print(','.join(str_list))



