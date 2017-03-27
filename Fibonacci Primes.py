x=int(input("Type in the nth term of the fibonacci number that you want: "))
a=1 #The Fibonacci numbers start out with two ones. 
b=1

number=0
summ=0

for i in range(0,x-2): #This is to account for some numbers tha will be left out during the calculations. 
    c=a+b
    
    prime="yes"
    for i in range (2,int(c**0.5)+1): #Using the square root of the number will greatly decrease the time  
        if (c%i)==0:
            prime="no"
  #This is used to check if a prime number exists by checking if it is divisible by the numbers under the square root.
    if prime =="yes":
      number+= 1 #to count the number of Fibonacci primes
      print(c)

    a=b
    b=c
print("There are", number, "Fibonacci Primes under the", x,"th Fibonacci sequence") 


            




