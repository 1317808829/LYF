x =float(input('x ='))
if x > 1 :                         
    y = 3 * x - 5
elif x >= -1 :
    y = x + 2
else : 
    y = 5 * x + 3
print('f(%.1f)= %.1f' % (x ,y))

from random import randint

face = randint(1 , 6)
if face == 1 :
    result = '排骨大串'
elif face == 2 :
    result = '刀削面'
elif face == 3 :
    result = '番瘸锅'
elif face == 4 :
    result = '成都味道'
elif face == 5 :
    result = '炸鸡'
elif face == 6 :
    result = '麻辣拌'
print(result)
#掷骰子选吃啥

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)


