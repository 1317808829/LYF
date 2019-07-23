#练习一 寻找水仙花数
for i in range(100,999):
    a = i % 10
    b = i // 10 % 10
    c = i // 100
    if i == a ** 3 + b ** 3 + c ** 3 :
        print(i , a , b , c )


#练习二 寻找完美数
import math 
import time

for num in range(1,10000):
    sum=0
    for factor in range(1, int(math.sqrt(num)+1 )):
        if num % factor == 0 :
            sum += factor 
            if factor >1 and num / factor != factor :
                sum += num / factor 
    if sum == num:
        print(num)


#练习三 百钱百鸡
#    5 * a + 3 * b = 100 -  ( 100 - a - b ) / 3
for a in range(0,20) :
    for b in range(0,33) :
        if 5 * a + 3 * b == 100 -  ( 100 - a - b ) / 3  :
            print ('%d,%d,%d' % ( a , b , (100-a-b)) )


#练习四  生成斐波那契数列
sum = 0 
a = 1
for x in range(1,20):
    a , sum = sum , sum + a 
    print(sum)