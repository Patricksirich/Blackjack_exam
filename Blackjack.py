from random import shuffle

#Our lists for the cards
card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']       
card_suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
#A dictionary translating our cards into the correct values
card_values = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10} #Dictionary

#The shuffled deck
deck = []

#Dealer and players hands
dealer_cards = []
player_cards = []


#Creates the deck with 52 cards
def create_deck():
    deck.clear()
    for suits in card_suits:
        for ranks in card_ranks:
            deck.append(ranks + " of " + suits)
#Shuffle the cards to create a random order in the deck
    shuffle(deck)
    return deck


#Removes last card from the deck[] and return the value
def deal():
    return deck.pop()


#Checks the card's value so that we can do a sum of the cards in the hand
def card_value(card_name):
    card_rank = card_name.split(" of ")
    return card_values[card_rank[0]]


#Checks whether there is an Ace in the hand and adjusts value
def check_for_ace(card_name, current_value):    
    if card_name.split(" of ")[0] == "A" and current_value + 11 > 21:
        return_value = 1
    else:
        return_value = card_value(card_name)
    return return_value


#Rules for dealing the cards as a player
def player_deal(player_value_local):
    playing = True
    current_value = player_value_local

    #While loop to ensure that the player gets as many hits as he wants
    while playing == True:
        draw = input("Hit Y/N: ")

        #If player chooses yes
        if str.lower(draw) == "y":
            player_cards.append(deal())
            player_value_local = 0
            #Iterate through the player_cards list so that we can check the sum and add the new card
            for i in player_cards:
                player_value_local += check_for_ace(i, current_value)

            print("You currently have ", player_value_local, "\n")
            print("Player cards:\n" + ' '.join(player_cards) + "\n===================================")
            current_value = player_value_local

             #Check is sum is over 21
            if player_value_local > 21:
                print("Player has busted\n")
                playing = False

        #If player wish to stand, break the loop    
        if str.lower(draw) == "n":
            playing = False

    #Return the local variable in the function so that we can change the global variable
    return player_value_local


#Rules for dealing the cards for the player
def dealer_deal(dealer_value_local):
    current_value = dealer_value_local
    print(dealer_value_local)
    #Forever loop so that we don't have to take any actions
    while True:
        #check if dealer goes above 16, if true then break the loop
        if dealer_value_local > 16:
            break 
        dealer_cards.append(deal())
        dealer_value_local = 0
        #Iterate through dealer_cards and find the value so that we can check the sum of the cards - also checks for aces
        for i in dealer_cards:
            dealer_value_local += check_for_ace(i, current_value)
        print("Dealer has: ", dealer_value_local, "\n")
        print("Dealer cards:\n" + ' '.join(dealer_cards) + "\n===================================")
        current_value = dealer_value_local

    #Return the local variable in the function so that we can change the global variable
    return dealer_value_local


#Function to start the game
def start_current_game():
    #Sets the dealer/player value to 0
    dealer_value_global = 0
    player_value_global = 0

    #Clears the list to ensure we get brand new cards
    player_cards.clear()
    dealer_cards.clear()

    #Add 2 cards to dealer and player in the correct order of the blackjack rules
    dealer_cards.append(deal())
    player_cards.append(deal())
    dealer_cards.append(deal())
    player_cards.append(deal())
    
    #Iterate through dealer_cards and find the value so that we can check the sum of the cards
    for i in dealer_cards:
        dealer_value_global += card_value(i)
    print(dealer_cards[0] + "  [HIDDEN CARD] + \n===================================")

    #Iterate through player_cards and find the value so that we can check the sum of the cards   
    for i in player_cards:
        player_value_global += card_value(i)

    if dealer_value_global == 21 and player_value_global == 21:
        print(dealer_cards[0] + "   " + dealer_cards [1])
        print(player_cards[0] + "   " + player_cards [1])
        return "Tie"

    elif player_value_global == 21:
        return "Player blackjack"

    print(player_cards[0] + "   " + player_cards[1])
    print("You currently have: ", player_value_global)

    #Call the player_deal() function, now the player can play
    player_value_global = player_deal(player_value_global)
    print("player value (global) 1: ", player_value_global)
    print(dealer_cards[0] + "   " + dealer_cards [1])
    if dealer_value_global == 21:
        print("Dealer got a blackjack!")
        return "Dealer"
    if player_value_global > 21:
        return "Dealer"

    #When the player is done playing, call dealer_deal() function, now the dealer plays
    dealer_value_global = dealer_deal(dealer_value_global)
    
    if dealer_value_global > player_value_global and dealer_value_global < 22:
        return "Dealer"
    elif player_value_global > dealer_value_global and player_value_global < 22:
        return "Player"
    elif dealer_value_global == player_value_global:
        return "Tie"
    elif dealer_value_global > 21:
        return "Player"


#Function that determines the rules of the game
def game_rules():
    game_round = 0

    if game_round == 0:
        chips = int(input("How much would like to start with: "))
        initial_chips = chips

    game_round += 1

    while game_round > 0:
        print("Your total amount of chips: ", chips)
        print("===================================")
        chips_betted = 0
        chips_betted = int(input("How much would you like to bet:\n"))
        print("You have betted: ", chips_betted)
        print("===================================")
        create_deck()
        result = start_current_game()
        
        if result == "Player blackjack":
            print("Blackjack - you win!")
            chips += (chips_betted * 1.5)
        if result == "Player":
            print("You won!")
            chips += chips_betted
        if result == "Dealer":
            print("Dealer has won")
            chips -= chips_betted
        if result == "Tie":
            print("It's a tie, you get your money back!")
            chips = chips
        if chips == 0:
            retry = input("You ran out of money, do you want to try again? Y/N\n")
            if str.lower(retry) == "y":
                print("Excellent choice!")
                game_round = 0
            else:
                print("Thank you for playing, have a nice day!")
                exit()
        continue_playing = input("Would you like to continue playing? Y/N\n")
        if str.lower(continue_playing) == "y":
            continue
        if str.lower(continue_playing) == "n":
            print("Thank you for playing! \nToday you have walked out with: ", chips - initial_chips, " chips!")
            exit()  


if __name__ == "__main__":
    #Call the game_rules() function to start the game
    game_rules()