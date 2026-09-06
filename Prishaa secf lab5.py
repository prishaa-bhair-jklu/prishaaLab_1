#lab5
#pro1
'''X=int(input("enter x"))
Y=int(input("enter y"))
N=int(input("enter N"))
for i in range(X,Y+1):
     if i%N==0:
        print(i)'''
        
#pro2
'''n=int(input("enter positive number"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
    print("sum of digits=",sum)'''
    
#pro3
'''N=int(input("enter N"))
divisible=0
not_div=0
while True:
    num=int(input("enter a number"))
    if num==-999:
        break
    if num%N==0:
        divisible+=1
    else:
        not_div+=1 
print("numbers divisible by N",divisible)
print("numbers not divisible by N",not_div)'''

    
#pro4
'''N=int(input("enter a positive integer"))
if N<0:
    print("invalid input")
else:
    factorial=1
    i=1 
    while i<=N:
       factorial=factorial*i  
       i=i+1 
    print("factorial",factorial)'''
    
    
#pro5
'''num=int(input("enter a positive integer"))
original=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")'''
    
#pro6
'''N=int(input("enter N"))
a=1
b=1
i=1
while i<=N:
    print(a, end=" ")
    c=a+b
    a=b
    b=c
    i+=1'''

#pro7
'''n=int(input("enter an integer"))
if n<=1:
    print("invalid input")
else:
    i=2 
    prime=True
    while i*i<=n: 
        if n%i==0:
            prime=False
            break
        i+=1
    if prime:
        print("prime no")
    else: 
        print("not a prime no")'''

     
#pro8
s=input("enter a sentence")
i=0
capital=0
small=0
digits=0
special=0
while i<len(s):
    ch=s[i]
    if 'A'<=ch<='Z':
        capital+=1 
    elif 'a'<=ch<='z':
        small+=1
    elif '0'<=ch<='9':
        digits+=1
    else:
        special+=1 
    i+=1 
print("capital letters:",capital)
print("small letters:",small)
print("digits:",digits)
print("special characters:",special)

    
    