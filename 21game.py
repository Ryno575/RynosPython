# 21 game
import random as rand
card_choices = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

reset = True
more_card = "Y"

player_score = 0
computer_score = 0
total_games = 0

# Begins Reset Loop
while reset == True:
    more_card = "Y"
# Computer gets two random cards
    computer_cards = []
    computer_cards.append(rand.choice(card_choices))
    computer_cards.append(rand.choice(card_choices))
# Player gets two random cards
    player_cards = []
    player_cards.append(rand.choice(card_choices))
    player_cards.append(rand.choice(card_choices))

# Asks the player if they would like another card, as long as the total is less than 20
    while more_card == "Y":
        player_cards_total = 0
        # Prints the total number of cards, as well as their values
        for i in range(len(player_cards)):
            print(f"Card {i + 1}: {player_cards[i]}")
            player_cards_total += player_cards[i]


        # If the score is over 21 and theres an 11 then it can be switched to a 1 (Like an Ace in the real 21 game)
        if (player_cards_total > 21) and (11 in player_cards):
            for i in range(len(player_cards)):
                if player_cards[i] == 11:
                    player_cards[i] = 1
                    player_cards_total -= 10
        
        print("")
        print(f"Total: {player_cards_total}")
        print("")

        # If the value is less than 20 -> user can add another card if they'd like
        if (player_cards_total) <= 20:
            more_card = input("Would you like another card? Y or N: ")
            if more_card == "Y":
                player_cards.append(rand.choice(card_choices))
                print("")
            else:
                more_card = ""
        else:
            more_card = ""

# The computer randomly can choose a new card
    more_card = "Y"
    while more_card == "Y":
        computer_cards_total = 0
        for i in range(len(computer_cards)):
            computer_cards_total += computer_cards[i]
        # If the score is over 21 and theres an 11 then it can be switched to a 1 (Like an Ace in the real 21 game)
        if (computer_cards_total > 21) and (11 in computer_cards):
            computer_cards_total = 0
            for i in range(len(computer_cards)):
                if computer_cards[i] == 11:
                    computer_cards[i] = 1
                computer_cards_total += computer_cards[i]
        
        if (computer_cards_total) <= 10:                              # If between 0 - 10 -> has a 90% chance of choosing a new card
            card_random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]            
            computer_random = rand.choice(card_random)        
            if computer_random >= 2:
                computer_cards.append(rand.choice(card_choices))
                print("The computer has picked a new card!")
                print("")
            else:
                more_card = ""                
                print("")
        elif (computer_cards_total) <= 15:                             # If between 11 - 15 -> has a 40% chance of choosing a new card
            card_random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            computer_random = rand.choice(card_random)        
            if computer_random >= 7:
                computer_cards.append(rand.choice(card_choices))
                print("The computer has picked a new card!")
                print("")
            else:
                more_card = ""
                print("")

        elif (computer_cards_total) <= 20:                             # If between 16 - 20 -> has a 10% chance of choosing a new card
            card_random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            computer_random = rand.choice(card_random)        
            if computer_random == 10:
                computer_cards.append(rand.choice(card_choices))
                print("The computer has picked a new card!")
                print("")
            else:
                more_card = ""
                print("")
        else:
            more_card = ""
    

# Decides the winner
    if player_cards_total > 21 and computer_cards_total > 21:             # IF both player and computer over 21 then no one wins
        print("You both lost!")
        print("Your score was: ", player_cards_total)
        print("The computer's score was: ", computer_cards_total)
        print("")
        total_games += 1
    elif player_cards_total > computer_cards_total:                       # Checks if the player has a higher card
        if player_cards_total > 21:                                       # If it is over 21 they lose
            print("You Lose!")
            print("Your score was: ", player_cards_total)
            print("The computer's score was: ", computer_cards_total)
            print("")
            computer_score += 1
            total_games += 1

        elif player_cards_total > 0 and player_cards_total <= 21:         # If it is between 0 and 21 they win
            print("You Win!!")
            print("Your score was: ", player_cards_total)
            print("The computer's score was: ", computer_cards_total)
            print("")
            player_score += 1
            total_games += 1

    elif computer_cards_total > player_cards_total:                       # Checks if the computer has a higher card
        if computer_cards_total > 21:                               # If it is over 21 they lose
            print("You Win!!")
            print("Your score was: ", player_cards_total)
            print("The computer's score was: ", computer_cards_total)
            print("")
            player_score += 1
            total_games += 1

        elif computer_cards_total > 0 and player_cards_total <= 21:       # If it is between 0 and 21 they win
            print("You Lose!!")
            print("Your score was: ", player_cards_total)
            print("The computer's score was: ", computer_cards_total)
            print("")
            computer_score += 1
            total_games += 1

    elif computer_cards_total == player_cards_total:                      # If they are the same they tie and no one wins
        print("You tied!!")
        print("Your score was: ", player_cards_total)
        print("The computer's score was: ", computer_cards_total)
        print("")
        total_games += 1
        

    reset = input("Would you like to reset? Y or N: ")
    print("")
    if reset == "N":
        reset = False
    else:
        reset = True

print("You won: ", player_score, " games!")
print("The computer won: ", computer_score, " games!")
print("You played: ", total_games, " games!")
print("")
print("Goodbye!")
