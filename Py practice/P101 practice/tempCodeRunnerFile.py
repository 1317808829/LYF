def factorial(num):
    result = 1
    for n in range (num):
        result *= n 
    return result

m = int(input('m ='))
n = int(input('n = ')) 

print(factorial(m) // factorial(n) // factorial(m - n ))
