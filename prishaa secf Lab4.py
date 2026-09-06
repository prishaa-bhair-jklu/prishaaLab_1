#lab4
'''salary=float(input("enter salary"))
years=int(input("years of service"))
if salary<0 or years<0:
    print("invalid input")
elif years>5:
    bonus=(salary*5)/100
    print("bonus amount=",bonus)
else:
    print("bonus amount=",0)'''
    
    
#pro2
'''password=input("enter password")
if password=="s3cr3t!P@ssw0rd":
    print("welcome")
else:
    print("wrong password")'''


#pro3
'''shape=input("enter shape(square,rectangle,circle,triangle")
if shape=="square":
    side=int(input("enter side"))
    if side<0:
        print("invalid inputs")
    else:
        area=side*side
        print("area=",round(area,3))
elif shape=="rectangle":
    l=int(input("enter l"))
    w=int(input("enter width"))
    if l<0 or w<0:
        print("invalid input")
    else:
        area=l*w
        print("area=",round(area,3))
elif shape=="circle":
    r=int(input("enter radius"))
    if r<0:
        print("invalid input")
    else:
        area=3.14*r*r
        print("area=",round(area,3))
elif shape=="triangle":
    b=int(input("enter base"))
    h=int(input("enter height"))
    if b<0 or h<0:
        print("invalid inputs")
    else:
        area=0.5*b*h
        print("area=",round(area,3))
else:
    print("invalid input")'''
    
    
#pro4
'''hours=int(input("enter hours"))
minutes=int(input('enter minutes'))
if hours<0 or hours>24 or minutes<0 or minutes>59:
    print("invalid input")
else:
    minutes=minutes+15
    if minutes>=60:
        minutes=minutes-60
        hours=hours+1
    if hours==24:
        hours=0
print(f"{hours:02d}:{minutes:02d}")'''


#pro5
'''n=float(input("enter distance in km"))
period=input("enter period that is day or night")
if n<0:
    print("invalid input")
elif period!="day" and period!="night":
    print("invalid input")
else:
    if period=="day":
        taxi=33.58+n*37.89
    else:
        taxi=33.58+n*43.17
    cheapest=taxi
    transport="taxi"
    
    if n>=20:
        bus=n*4.32
        if bus<cheapest:
            cheapest=bus
            transport="bus"
    if n>=100:
        train=n*2.88
        if train<cheapest:
             cheapest=train
             transport="train"
    print("cheapest transport:",transport)
    print("price:",round(cheapest,2),"BGN")'''

    
#pro6
'''h=int(input("enter number of holidays"))
workdays=365-h
w_games=workdays*63
h_games=h*127

tot_games=w_games+h_games
norm=30000
if tot_games<=norm:
    difference=norm-tot_games
    print("tom sleeps well")
    print("difference:",difference)
else:
    difference=tot_games-norm
    print("tom will not sleep well")
    print("difference:",difference)'''
    
#pro7
'''budget=float(input())
season=input()
if budget<0 :
     print("invalid input")
elif season!="summer" and season!="winter":
     print("invalid input")
else:
     if budget<=100:
        dest="bulgaria"
        
        if season=="summer":
           place="camp"
           spent=budget*0.30
        else:
          place="hotel"
          spent=budget*0.70
     elif budget<=1000:
          dest="balkans"
         
         if season=="summer":
            place="camp"
            spent=budget*0.40
         else:
          place="hotel"
          spent=budget*0.80
    else:
        dest="europe"
        place="hotel"
        spent=budget*0.90
    print("somewhere in ",dest)
    print(f"{place}-{spent:.2f}")'''

#pro8
'''for number in range(1,1000):
    if number%10==6:
        print(number)'''
        
#pro9
'''n=int(input("enter n"))
total=0
for i in range(n):
    num=int(input(("enter number")))
    total=total+num
    print("sum",total)'''
    
#pro10
N=int(input("enter pos number"))
if N<=0:
    print("invalid input")
else:
    for i in range(1,21):
        print(N,"x",i,"=",N*i)
        
         