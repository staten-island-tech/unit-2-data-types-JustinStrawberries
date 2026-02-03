def discount(IsMember, Age, IsResident):
    if Age < 12 or Age >= 60:
        if (IsResident == True or IsMember == True):
            print('Yes discount')
    else:
        print ('No dicount)')
    
discount(True, 12, False)