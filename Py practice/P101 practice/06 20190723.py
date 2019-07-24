m = int (input('m= '))
n = int (input('n= '))
fm = 1
for num in range(1 , m + 1 ) :
    fm *= num 
fn = 1
for num in range(1, n + 1) :
    fn *= num 
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num 
print (fm // fn // fmn )

m = int(input('m= '))
for _ in range (1,m):
    print(_)

def fac(num):
    result = 1
    for n in range (1, num +1):
        result *= n
    return result 

m = int(input('m ='))
n = int(input('n= '))

print(fac(m) // fac(n) // fac(m-n))
# 排列组合

from random import randint

def roll_dice(n=3):
    total = 0
    for _ in range(1, 6):
        total += randint(1,6)
    return total
print(roll_dice(4))
#掷骰子 默认值3颗


def add(a=0, b=0, c=0):
    return a + b + c

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3, 4))


def addd(*a):
    total = 0 
    for val in a:
        total += val
    return total

print(addd(1, 3, 6, 10))

def gcd(x, y):
    if x > y :
        (x, y) = (y, x )
    for factor in range(x, 0, -1):
        if x % factor ==0 and y % factor == 0:
            return factor
def lcm(x ,y):
    return x * y // gcd(x, y)

print(gcd(16,44))
print(lcm(16,44))


