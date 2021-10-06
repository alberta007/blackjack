import random
import os

def hand(x):
    sum = 0
    
    ej_ess = [kort for kort in x if kort != 'A'] #Gör en lista för alla kort som inte är ess
    ess = [kort for kort in x if kort == 'A']    #Gör en lista för alla kort som ÄR ess
    
    for kort in ej_ess:
        if kort == 'J' or kort == 'Q' or kort == 'K': #Om kortet i listan ej_spader är J, Q eller K så läggs det till 10 poäng i sum
            sum += 10
        else:
            sum += int(kort)                   #Om kortet inte är J Q eller K så adderas kortets nummer till summan
            
    for kort in ess:
        if sum <= 10:
            sum += 11
        else:
            sum += 1
            
    return sum


gameloop = True

while gameloop:
    

    kort = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4


        
    random.shuffle(kort)

    dealer = []
    spelare = []



    standing = False
    first_hand = True

    spelare.append(kort.pop())
    dealer.append(kort.pop())
    spelare.append(kort.pop())
    dealer.append(kort.pop())

    while True:
        
        clear = "\n" * 100
        spelare_points = hand(spelare)
        dealer_points = hand(dealer)
        
        print(clear)
        
        print("Välkommen till blackjack!\n")

        print("Dina kort:", spelare, spelare_points)
        
        if standing:
            print("Dealerns kort: ", dealer, dealer_points)
        else:
            print("Dealerns kort: ", [dealer[0],'?'])
            
        if standing:
            
            if dealer_points > 21:
                print("Du vinner!")
            elif spelare_points == dealer_points:  
                print("Ingen vinner, du får pengarna tillbaka")               
            elif spelare_points > dealer_points:
                print("Grattis du vinner!")                    
            else:
                print("Du förlorade")
                
            fort = input("\nVill du spela igen? [Y/N] ")
                
            if fort == 'Y':
                    gameloop = True
            elif fort == 'N':
                gameloop = False
            break
        
        if first_hand and spelare_points == 21:
            print("Blackjack! Du är rik!")
            break
        
        if spelare_points > 21:
            print("Du förlorade!")
            break
        
        print("[1] Hit\n[2] Stand")
        val = input("Välj ett alternativ: ")
        
        if val == '1':
            spelare.append(kort.pop())
        elif val == '2':
            standing = True
            while hand(dealer) <= 16:
                dealer.append(kort.pop())
    
        
    if gameloop == False:
        print("\nTack för att du spelade!")
        break
        
    
    