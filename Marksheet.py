print("Enter name:")
name=input()
print("Enter Maths marks")
M=float(input())
if(M>=0 and M<=100):
    print("Enter Hindi marks")
    H=float(input())
    if(H>=0 and H<=100):
        print("Enter English marks")
        E=float(input())
        if(E>=0 and E<=100):
            print("Enter Science marks")
            SC=float(input())
            if(SC>=0 and SC<=100):
                print("Enter Social studies marks")
                SST=float(input())
            else:
                print("Enter valid marks")
        else:
            print("Enter valid marks")
    else:
        print("Enter valid marks")
else:
    print("Enter valid marks")
Total=M+H+E+SC+SST
Perc=Total/5
counter=0
print("\nName: ",name)
print("\nSubject\t\tT.M\t\tObt.M\t\tStatus")
if(M>=33.00):
    status="Pass"
    print("Maths\t\t100\t\t",M,"\t\t",status)
else:
    status="Fail"
    print("Maths\t\t100\t\t",M,"\t\t",status)
    counter+=1
if(H>=33.00):
    status="Pass"
    print("Hindi\t\t100\t\t",H,"\t\t",status)
else:
    status="Fail"
    print("Hindi\t\t100\t\t",M,"\t\t",status)
    counter+=1
if(E>=33.00):
    status="Pass"
    print("English\t\t100\t\t",E,"\t\t",status)
else:
    status="Fail"
    print("English\t\t100\t\t",M,"\t\t",status)
    counter+=1
if(SC>=33.00):
    status="Pass"
    print("Science\t\t100\t\t",SC,"\t\t",status)
else:
    status="Fail"
    print("Science\t\t100\t\t",M,"\t\t",status)
    counter+=1
if(SST>=33.00):
    status="Pass"
    print("Soc.St.\t\t100\t\t",SST,"\t\t",status)
else:
    status="Fail"
    print("Soc.St.\t\t100\t\t",M,"\t\t",status)
    counter+=1
print("\t Total\t500\t\t",Total)
if(counter==0):
    if(Perc>=60):
        print("\n\tPercentege: ",Perc,"%   Division: I")
    elif(Perc>=45):
        print("\n\tPercentege: ",Perc,"%   Division: II")
    elif(Perc>=33):
        print("\n\tPercentege: ",Perc,"%   Division: III")
    else:
        print("\n\t Fail")
else:
    print("\n\t  Fail")

    

    
        
        
        
            
            