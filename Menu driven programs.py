#*********************Menu Driven Program 1*********************
#print("Enter 1 to check whether a number is even or odd")
#print("Enter 2 to check whether an year is leap year or not")
#print("Enter 3 to check whether a 3 digit number is palindrome or not")
#print("\nEnter your choice:")
#ch=int(input())
#if(ch==1):
#    print("Enter a no.")
#    n=int(input())
#    if(n%2==0):
#        print("Number is even")
#    else:
#        print("Number is odd")
#elif(ch==2):
#    print("Enter an year")
#    yr=int(input())
#    if(yr%4==0):
#        print("Leap year")
#    else:
#        print("Not leap year")
#elif(ch==3):
#    print("Enter a 3 digit number")
#    n=int(input())
#    if(n>=100 and n<=999):
#        if(n%10==n//100):
#            print("Number is palindrome")
#        else:
#            print("Number is not palindrome")
#    else:
#        print("Enter correct digit number")
#else:
#    print("Enter valid number")
           
#***********************Menu Driven Program 2********************
print("Enter 1 to convert Celcius into Fahrenheit and Farenheit into Celcius")           
print("Enter 2 to convert Seconds to Minute to Hour")           
print("Enter 3 to convert Metre into kilometre and kilometre into metre")   
print("\nEnter your choice:")
ch=int(input())
if(ch==1):
    print("Enter 1.1 to convert Celcius into Fahrenheit")
    print("Enter 1.2 to convert Farenheit into Celcius")  
    print("\nEnter your choice:")
    ch1=float(input())      
    if(ch1==1.1):
        print("Enter temperature")
        celcius=float(input())
        fahrenheit=((9/5)*celcius+32)
        print("Temperature in Fahrenheit = ",fahrenheit)
    elif(ch1==1.2):
        print("Enter temperature")
        fahrenheit=float(input())
        celcius=(5/9*(fahrenheit-32))
        print("Temperature in Celcius = ",celcius)
    else:
        print("Enter valid number")
elif(ch==2):
    print("Enter time in seconds")
    time=int(input())
    sec=time%60
    min=(time//60)%60
    hr=(time//60)//60
    print("Hour(s) = ",hr)
    print("Minute(s) = ",min)
    print("Second(s) = ",sec)
elif(ch==3):
    print("Enter 1.1 to convert meter into kilometre")
    print("Enter 1.2 to convert kilometer into metre")
    print("\nEnter your choice")
    ch1=float(input())
    if(ch1==1.1):
        print("Enter distance:")
        m=int(input())
        km=m/1000
        print("Distance in kilometre = ",km,"km")
    elif(ch1==1.2):
        print("Enter distance:")
        km=int(input())
        m=km*1000
        print("Distance in metre = ",m,"m")
    else:
        print("Enter valid number")
else:
    print("Enter valid number")
    

    
        
        
        
