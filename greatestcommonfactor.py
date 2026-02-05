


number = int(input("enter a number"))

numbertwo = int(input("enter another number"))


factor = [1,number]
factor2 = [1,numbertwo]

for i in range(2,number):
    if(number % i ==0):
        print (i)
        factor.append(i)

for i in range(2,numbertwo):
    if(numbertwo % i ==0):
        print (i)
        factor2.append(i)

print(factor,factor2)

greatestfactor = [factor == factor2]

print(greatestfactor)