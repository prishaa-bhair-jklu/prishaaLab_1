#lab3
#pro1
'''x1=float(input("enter first point of center of circle:"))
y1=float(input("enter second point of center of circle:"))
r=float(input("enter radius :"))
x2=float(input("enter another first point:"))
y2=float(input("enter another second point:"))
d= (((x2-x1)**2+(y2-y1)**2)**(1/2))
if d<r:
    print("point lies inside the circle")
elif d==r:
    print("point lies on the boundary of circle")
else:
    print("point lies outside the circle")'''


#pro2

'''s=float(input("enter side of pentagon:"))
area=(5*s**2)/(4*0.72654)
print(area)'''


#pro3
'''a=int(input('enter first angle'))
b=int(input("enter second angle"))
c=int(input("enter third angle"))
if a<=0 or b<=0 or c<=0:
    print("invalid input")
elif a+b+c != 180:
    print("angles cannot form triangle")
elif a<90 and b<90 and c<90:
    print("acute angled triangle")
elif a==90 or b==90 or c==90:
    print("right angled triangle")
else:
    print("obtuse angled triangle")'''
    
    
#pro4
'''num=int(input("enter 4 digit number"))
f=num//100
l=num%100
sumf = (f//10)+(f%10)
suml= (l//10)+(l%10)
print(sumf)    
print(suml)
if sumf==suml:
    print("sum are equal")
else:
    print("sum are not equal")'''
    

#pro5
'''num=int(input("enter 5 digit number"))
a=num//10000
b=(num//1000)%10
c=(num//100)%10
d=(num//10)%10
e=num%10
if a>=b and a>=c and a>=d and a>=e:
    largest =a
    position =1
elif b>=c and b>=d and b>=c and b>=d and b>=e:
    largest=b
    position =2
elif c>=d and c>=e:
    largest=c
    position =3
elif d>=e:
    largest=d
    position =4
else:
    largest=e
    position= 5
print(largest)
print(position)'''


#pro6
'''a=int(input("enter first digit"))
b=int(input("enter second digit"))
c=int(input("enter the third digit"))
print("before rotation")
print("a=",a)
print("b=",b)
print("c=",c)
a=a+b+c
b=a-b-c
c=a-b-c
a=a-b-c
print("after rotation")
print("a=",a)
print("b=",b)
print("c=",c)'''


#pro7
'''num=int(input("enter three digit number"))
a=num//100
b=(num//10)%10
c=num%10
summ=a+b+c
if num%summ==0:
    print("it is a harshad number")
else:
    print("it is not a harshad number")'''


#pro8
'''v=float(input("enter initial volume of water")) 
n=int(input("enter the number of days"))    
w=200+(v-200)*0.95**n
if v<0 or n<0:
    print("invalid inputs")
else:
    print("quantity of water in",n,"days",w)'''
    

#pro9
'''a1=float(input("enter a1:"))
b1=float(input("enter b2:"))
c1=float(input("enter c1:"))
a2=float(input("enter a2:"))
b2=float(input("enter b2:"))
c2=float(input("enter c3:"))
d=a1*b2-a2*b1
if d!=0:
    x=(c1*b2-c2*b1)/d
    y=(a1*c2-a2*c1)/d
    print("lines intersect at:")
    print("x=",round(x,2))
    print("y=",round(y,2))
else:
    dx=a1*c2-a2*c1
    dy=b1*c2-b2*c1
    if dx==0 and dy==0:
        print("lines are coincident")
    else:
        print("lines are parallel")'''
    
    







