#que1
'''print("     Addition table")
print("   ",end="")
for j in range(1,10):
    print(f"{j:3}",end="")
print()
print("------------------------------")
for i in range(1,10):
    print(f"{i} |",end="")
    for j in range(1,10):
        print(f"{i+j:3}",end="")

    print()'''
    
#que2
'''n=int(input("enter number"))
if n<1 or n>1000:
    print("invalid input")
else:
    slot=n
    while slot<=1000:
        if slot%4==0:
            slot+=n
            continue
        print(slot,end="")
        slot+=n'''
        
#que3
'''n=int(input("enter number"))
if n<=0:
    print("invalid inputs")
else:
    i=1 
    while i<=n:
        j=1 
        while j<=i:
            print(j,end=" ")
            j+=1 
        print()
        i+=1'''
        
'''n=int(input("enter num"))
if n<=0:
    print("invalid input")
else:
    i=n
    while i>=1:
        j=1 
        while j<=i:
            print("*",end=" ")
            j+=1
        print()
        i-=1'''
        
'''n=int(input("enter num"))
if n<=0:
    print("invalid input")
else:
    i=1 
    while i <= n:
        space=n-i
        while space>0:
            print("  ",end="")
            space -= 1
        j=1 
        while j<=1:
            print("*",end=" ")
            j+=1 
        print()
        i+=1'''
            
#que4
'''n=int(input("enter num"))
if n<=0:
    print("invalid input")
else:
    octal=" "
    while n>0:
        remainder=n%8
        octal=str(remainder)+octal
        n=n//8
    print("octal equivalents:",octal)'''
    
#que5
'''n=int(input("enter num"))
distances=[]
for i in range (n):
    distance=int(input())
    distances.append(distance)
winning=max(distances)
runner_up=0
for distance in distances:
    if distance<winning and distance>runner_up:
        runner_up=distance
print(winning)
print(runner_up)'''

#que6
'''n=int(input("enter num"))
for num in range(1,n+1):
    temp=num
    digit=len(str(num))
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**3  
        temp=temp//10
    if total==num:
        print(num)'''
        
#que7
'''for n in range(1,16):
    square=n**2 
    cube=n**3 
    root=n**0.5 
    print(n,"\t",square,"\t",cube,"\t",format(root,".4f"))'''
    
#que8
'''n=int(input("enter num"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
        for j in range(i):
            print(i,end=" ")
        print()'''
        
#que9
'''n=int(input("enter num"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()'''
    
#que10
n=int(input("enter number"))
for i in range(i,n+1,2):
    for j in range((n-i)//2):
        print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
for i in range(n-2,0,-2):
    for j in range((n-i)//2):
        print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        print()
    