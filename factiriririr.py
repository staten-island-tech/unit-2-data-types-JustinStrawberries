
number = int(input("enter a number"))
# number = str(number)
# print("1 ," + number)

# if (number % 2 > 0):
#     print ('2')
# if (number % 3 > 0):
#     print ('3')

factor = []

for i in range(2,number):
    if(number % i == 0):
        print (i)
        factor.append(i)

print(factor)