#Finding Primes Using FLT
#Luis Loja
#January 1, 2017


#this program will use similar codes for the other types of prime numbers
#using fermats little theorem
ans="y"
while ans=="y":
    print()
    print("Hello, we are doing to be determining if one if a number is prime."
          "  Then we are going to look at the first twin, cousin and sexy primes below the index number of a prime")
    print()

    choice=input("Type(a)if you are trying to check if a number is prime." #Asking the user what he/she wants
    " Type(b) if you are trying to find twin primes."
    " Type(c)if you are trying to find cousin prime."
    " Type (d) if you are trying to find sexy primes:  ")

    if choice=="a":  #If the user wants to check the primality of a number
       print()
       a=int(input("Enter what number you want to determine the primality of: "))  #User enters any number
       if a==1:
           print(a,"is not prime nor composite.")  #This is if they type in one, because it is neither prime nor composite 
           break
       if(2**(a-1)%a)==1:   #First check to see if the entered number is prime
        for i in range(2,int(a**0.5)+1):  #check if it is a pseudoprime
             if (a%i)==0:
                print(a,"is not prime!It is a pseudoprime.")
                break
        else:
             print(a,"is prime")
       else:
          print(a,"is composite")

    if choice=="b":   #If the user wants to find twin primes
        print()
        count=2
        p=3 
        b=int(input("Enter the max prime index number that the twin primes can be:  "))
        while count<b+2:
            if(2**(p-1)%p)==1:
               count+=1
               if(2**(p+1)%(p+2))==1: #To find twin primes
                for i in range(2,int(p**0.5)+1):  #check if it is a pseudoprime
                    if (p%i)==0:
                        count-=1       
                        break
                else:
                    print(p,"and",p+2,"are twin primes") #This prints the twin primes
            p+=1
      
    if choice=="c": #If the user wants to find cousin primes
        print()
        count=2
        p=3 
        c=int(input("Enter the max prime index number that the cousin primes can be:  "))
        while count<c+2:
            if(2**(p-1)%p)==1:
               count+=1
               if(2**(p+3)%(p+4))==1: #To find cousin primes
                    for i in range(2,int(p**0.5)+1):  #check if it is a pseudoprime
                        if (p%i)==0:
                            count-=1       
                            break
                    else:
                        print(p,"and",p+4,"are cousin primes") #This prints the cousin primes
            p+=1

    if choice=="d":  #If the user wants to find sexy primes
        print()
        count=2
        p=3 
        d=int(input("Enter the max prime index number that the sexy primes can be:  "))
        while count<d+2:
            if(2**(p-1)%p)==1:
               count+=1
               if(2**(p+5)%(p+6))==1: #To find sexy primes
                    for i in range(2,int(p**0.5)+1):  #check if it is a pseudoprime
                        if (p%i)==0:
                            count-=1       
                            break
                    else:
                        print(p,"and",p+6,"are sexy primes") #This prints the sexy primes
            p+=1
    print()
    ans=input("Would you like to do this again? (y)es or (n)o: ")  #If the user wants to do this again





