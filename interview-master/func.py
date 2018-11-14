# 使用 while 循环打印 1 3 5 7 9

i = 1
while i <= 9:
    print(i, end=' ')
    i += 2
print('\n**************')

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1, 5, 7, 8, 9]
if 6 in l:
    print('found')
else:
    print('not found')
print('**************')
# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"
s1_list = []
s2_list = []
for item in s:
    if '0' <= item <= '9':
        s2_list.append(item)
    else:
        s1_list.append(item)
    s1 = ''.join(s1_list).lower()
    s = list(s1)
    str1 = s.sort()
    s1 = (''.join(s))
    s2_list.sort()
    s2 = ''.join(s2_list)
print(s1, s2)
