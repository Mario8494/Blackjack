import random 

def dealerHand():
    dcard1 = random.randint(1, 10)
    dcard2 = random.randint(1, 10)
    ddeck = card1 + card2
    show = random.randit(1, 2)
    if(show == 1):
        print("Dealer has a " + str(dcard1))
        
    
    

def playerHand():
    pcard1 = random.randint(1, 10)
    pcard2 = random.randint(1, 10)
    if(pcard1 == pcard2):
        pcard2 == random.randint(1, 10)
    pdeck = card1 + card2
    phs1 = input("Your total is " + str(pdeck) ". Hit or stay? (H/S)")
    if(phs1 == "H"):
        pcard3 = random.randint(1, 10)
        pdeck = pcard1 + pcard2 + pcard3
        if(pdeck > 21):
            print("Lol, you lost")
        else:
            phs2 = print("Your total is " + str(pdeck) + ". Hit or stay? (H/S)")
            if(phs2 == "H"):
                pcard4 = random.randint(1, 10)
                pdeck = pcard1 + pcard2 + card3 + card4 
                if(pdeck > 21):
                    print("Lol, you lost")
                else:
                    phs3 = print("Your total is " + str(pdeck) + ". Hit or stay? (H/S")
                    if(phs3 == "H"):
                        pcard5 = random.randint(1, 10)
                        pdeck = pcard1 + pcard2 + card3 + card4 
                        if(pdeck > 21):
                            print("Lol, you lost")
                        else:
                            phs3 = print("Your total is " + str(pdeck) + ". Hit or stay? (H/S")

            
    elif(phs1 == "S"):
        print("Your total: " + str(pdeck))
        print("Dealer's total: " + str)

    
