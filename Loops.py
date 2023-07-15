''' 
Program to print numbers from 1-10 
i=1
while i<=10:
    print(i)
    i+=1
'''

'''
Program to calculate first 10 Natural numbers

i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1
print(sum)
'''
#Program to print multiplication table of num #
'''
a=int(input())
for i in range(1,11):
    print(i*a)
'''
'''
Factorial Value
num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
'''
'''
Power of another
a=int(input())
b=int(input())
result=1
for b in range(b,0,-1):
    result *= a
print(result)
'''
a=int(input())
b=int(input())
result = pow(a,b)
print(result)