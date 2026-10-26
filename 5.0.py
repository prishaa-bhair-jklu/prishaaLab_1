#lab5.0
#pro1
'''x=int(input("enter x"))
y=int(input("enter y"))
N=int(input("enter N"))
count=0
for i in range(x,y+1):
    if i%N!=0:
        print(i,end=" ")
        count+=1 
print()
print(count)'''
    
#pro2
'''n=int(input("enter number"))
product=1
while n>0: 
    digit=n%10
    product=product*digit
    n=n//10
print(product)'''

#pro3
'''N=int(input("enter N"))
large=0
small=0
bill=int(input("enter bill"))
while bill!=-999:
    if bill>N: 
        large+=1 
    else: 
        small+=1
        
    bill=int(input())
print(large)
print(small)'''

#pro4
'''N=int(input("enter N"))
P=int(input("enter P"))
if N<=0 or P<0: 
    print("invalid input")
else:
    result=1 
    i=1 
    while i<=P:
        result=result*N
        i=i+1 
    print(result)'''
    
#pro5
'''x=int(input("enter x"))
y=int(input("enter y"))
original=x
reverse=0
while x>0:
    digit=x%10
    reverse=reverse*10+digit
    x=x//10
if reverse==y:
    print("yes")
else:
    print("no")'''

#pro6
'''n=int(input("enter n"))   
power=1
i=1
while i<=n:
    print(power,end=" ")
    power=power*2 
    i=i+1 '''
    
#pro7
'''n=int(input("enter n"))
sum=0
for i in range (1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")'''
    
#pro8
'''n=int(input("enter n"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()'''
    
#pro9
'''n=int(input("enter a pos integer"))
d=int(input("enter a digit"))
count=0
while n>0:
    digit=n%10
    if digit==d:
        count=count+1 
    n=n//10
print("digit appears",count,"times")'''

#pro10
n=int(input("enter N"))
count=0 
for i in range(1,n+1):
    if n%i==0 :
        print(i)
        count+=1 
print('total divisors',count)
if count==2:
    print("prime no")
else:
    print("not a prime no")

