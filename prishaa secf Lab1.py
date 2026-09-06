# lab 1 
#pro1
#print("Hello jklu !")
#print("I am learning python.")


#pro2
#a=input("enter your name")
#b=input("enter your branch")
#print("welcome! \n",a)

#pro3
#a=int(input("enter length of rectangle in metres"))
#b=int(input("enter widt of rectangle in metres"))
#area=a*b
#print(area)


#pro4
#a=int(input("enter length of rectangle in feet"))
#b=int(input("enter width of rectangle in feet"))
#area_sqfeet=a*b
#area_metres=area_sqfeet*0.3048
#print("area of rectangle in square metres= ",area_metres)


#pro5
#x=int(input("enter first positive integer "))
#y=int(input("enter second positive integer"))
#if x>0 and y>0:
   # if y%x==0:
      #  print("y is divisible by x")
    #else:
      #  print("y is not divisible by x")
#else:
    # print("invalid inputs")   

#pro6
#num=int(input("enter an integer"))
#if num%2==0:
    #print(num,"is even")
#else:
   # print(num,"is odd")
   
   
#pro7   
#radius=float(input("enter radius(1-100):")) 
#if radius<1 or radius>100:
    #print("invalid input")
#else:
    #area=3.14 * radius ** 2
   # print("area of circle : ", area)
   
#pro8   
#celius=float(input("enter temperature in celius"))
#fahrenheit=(celius   * 9/5)+32
#kelvin= celius+273.15
#print("Temperature in fahrenheit :",fahrenheit)
#print("Temperature in kelvin :",kelvin) 
   
   
#pro9
sec=int(input("enter seconds(1-86400):")) 
hours=sec//3600
minutes=(sec%3600)//60
sec=sec%60
if sec<=1 or sec>=86400:
    print("invalid input")
else:
    print(f"{hours}:{minutes}:{sec}:")
 
 
 
 
#mini challenge
tot_classes=int(input("enter total number of classes"))
attended=int(input("enter number of classes attended"))
if tot_classes<=0 or attended<0 or attended>tot_classes:
    print("invalid input")
else:
    attendance=(attended/tot_classes)*100
    print("Att Percentage :",attendance,"%")
    if attendance >=75:
        print("eligible")
    else:
        print("not eligible")
    
   
   
   
   
   
   
   
   