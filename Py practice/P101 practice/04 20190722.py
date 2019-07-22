sum = 0
for x in range(100):
    sum += x
print(sum)


import random

answer = random.randint(1,100)
counter = 0
while True :
    counter += 1
    number = int(input('请输入：'))
    if number < answer :
        print('大一点')
    elif number > answer :
        print('小一点')
    else:
        print('对了')
        break
print('你总共猜了%.1f次' % (counter))
#100以内猜数字


for i in range(1, 10):
    for j in range(1, i+1 ):
        print('%d*%d=%d' % (i , j ,  i*j ),end='\t')
    print()

# end='\t' 空四格不换行
