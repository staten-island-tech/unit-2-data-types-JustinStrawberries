

bill = float(input("Bill Cost"))

service = input("the service was bad, okay, good, or great")
# def service(bad, okay, good, great):
if (service == "bad"):
        print ('10%')
        finalbill = bill*1
        print(finalbill)
if (service == "okay"):
        print ('15%')
        finalbill = bill*1.15
        print(finalbill)
if (service == "good"):
        print ('20%')
        finalbill = bill*1.2
        print(finalbill)
if (service == "great"):
        print ('25%')
        finalbill = bill*1.25
        print(finalbill)