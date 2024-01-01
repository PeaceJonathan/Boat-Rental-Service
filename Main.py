
while True:
    
    #Intro
    
    print(f"Welcome to Python's Pontoons\n") 

    # USER INPUTS

    while True:
        PeopleSailing = input("Number of People going on the Boat? ")
        try:
            PeopleSailing = int(PeopleSailing)
            break
        except ValueError:
            print("Please enter a Number ")
    while True:
        DaysSailing = input("Number of Days you will be Sailing? ")
        try:
            DaysSailing = int(DaysSailing)
            break
        except ValueError:
            print("Please enter a Number ")
     
    while True:
        WhatBoat = int(input("Would you like a 30 or 40 foot Boat? "))
        if WhatBoat == 30 or WhatBoat == 40:
            break
        else :
            print("Please enter either 30 or 40 ")

    while True:    
        YachtClub = input("Are you a memeber of the Yacht Club? (y/n) ")
        if YachtClub == "y" or YachtClub == "n":
            break
        else :
            print("Please enter either y or n ")
            
    while True:    
        ScubaGear = input("Would you like Scuba Gear? (y/n) ")
        if ScubaGear == "y" or ScubaGear == "n":
            break
        else :
            print("Please enter either y or n ")

    #OUTPUT

    
    #DATE
            
    from datetime import datetime

    time1 = datetime.now().replace(microsecond = 0)
    print(f"\n\nReceipt\n")
    print(time1,f"\n")


    #NEW VARIABLES

    if WhatBoat == 30:
        BoatPrice = 100
    elif WhatBoat == 40:
        BoatPrice = 150
        
    #Totals
        
    BoatTotal = ((BoatPrice*PeopleSailing)*DaysSailing)
    print(f"Boat Total             :$ {round(BoatTotal,2)}")

    ScubaTotal = (PeopleSailing*45)
    if ScubaGear == "n":
        pass
    else:
        print(f"Scuba Gear Total       :$ {round(ScubaTotal,2)}")

    SubTotal = ScubaTotal+BoatTotal
    print(f"Sub Total              :$ {round(SubTotal,2)}")

    TotalTaxes = SubTotal * .095
    print(f"Tax 9.5%               :$ {round(TotalTaxes,2)}") 

    TotalDue = TotalTaxes + SubTotal
    print(f"Total Due              :$ {round(TotalDue,2)}")

    if YachtClub == "y":
        YachtDiscount = .85
        print("Yacht Club Discount    : 15%")
        GrandTotal = TotalDue * YachtDiscount
        print(f"Grand Total            :$ {round(GrandTotal,2)}")
    else :
        YachtDiscount = 1
        
    # To continue or quit
        
    while True:
        UserChoice = input(f"\nDo you want to quit (Q) or continue with another transaction (C)? ")
        if UserChoice.lower() == 'q':
            print("Goodbye")
            quit()
        elif UserChoice.lower() == 'c':
            print(f"\n")
            break  
        else:
            print("Invalid input. Please enter 'q' to quit or 'c' to process another transaction.")        
          




