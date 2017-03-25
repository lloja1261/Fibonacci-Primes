#Luis Loja
#Program 4: Determining a Prime Number
#November 25, 2016


ans="y"
while ans=="y": #Loop if user wishes to restart this program
    number=0
    summ=0
    n=int(input("Enter a positive integer: "))
    prime="yes"
    for i in range (2,int(n**0.5)+1): #User the square root of the number to look for different cases
        if (n%i)==0:
            print(n,"is not prime")
            prime="no"
            break
        
    if prime =="yes":
        print(n,"is prime!")

    if prime=="no":
        for i in range(1,n+1):
            if (n%i)==0:
                summ+=i
                number+=1
                print(i,"is a divisor of",n)
        print("The sum of all the divisors for",n,"is",summ)
        print("There are",number,"divisors for",n)
    
    ans=input("Do you want to do this again. Type (y)es or (n)o?:")
if ans=="n":
    print("End")






