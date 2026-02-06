


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

commonfactor = []

for i in factor:
    if i in factor2:
        commonfactor.append(i)

gcf = str(max(commonfactor))
print("Greatest Common Factor is " + gcf)