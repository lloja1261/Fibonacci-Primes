x=int(input("Type in the nth term of the fibonacci number that you want: "))
a=1
b=1


number=0
summ=0



for i in range(0,x-2):
    c=a+b
    
    prime="yes"
    for i in range (2,int(c**0.5)+1):
        if (c%i)==0:
            prime="no"
    if prime =="yes":
      number+= 1
      print(c)

    a=b
    b=c
print("There are", number, "Fibonacci Primes under the", x,"th Fibonacci sequence") 


            




