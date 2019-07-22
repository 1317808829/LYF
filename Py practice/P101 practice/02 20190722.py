a = int(input('a = '))
b = int(input('b = '))
print('%d + %d =%d' % (a, b,  a+b))
print('%d // %d =%d' % (a, b, a//b))

a = 100
b = 12.35
c = 1+ 5j
d = 'hello wordl'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)
#复合运算

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ",flag1)
print("flag2 = ",flag2)
print("flag3 = ",flag3)
print("flag4 = ",flag4)
print("flag5 = ",flag5)
print(flag1 is True)
print(flag1 is not False)

f = float(input('输入华氏温度'))
c = (f - 32)/ 1.8
print('%.1f 华氏度 = %.1f摄氏度' %(f, c ))
#华氏度摄氏度转化


import math

radius = float(input('输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长= %.2f' % perimeter)
print('面积= %.2f' % area)

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)