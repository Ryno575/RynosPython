# 21 game
import random as rand
import secrets
card_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

reset = True

player_score = 0
computer_score = 0
total_games = 0

# Begins Reset Loop
while reset == True:
# Computer gets two random cards
    computer_card1 = rand.choice(card_choices)
    computer_card2 = rand.choice(card_choices)
    computer_card3 = 0
# Player gets two random cards
    player_card1 = rand.choice(card_choices)
    player_card2 = rand.choice(card_choices)
    player_card3 = 0
# Asks the player if they would like another card
    print("Your cards are: ", player_card1, " and ", player_card2)
    if (player_card1 + player_card2) <= 20:
        more_card = input("Would you like another card? Y or N: ")
        if more_card == "Y":
            player_card3 = rand.choice(card_choices)
            print("Your new card is: ", player_card3)
            print("")
        else:
            print("")
    player_cards = (player_card1 + player_card2 + player_card3)

# The computer randomly can choose a new card
    if (computer_card1 + computer_card2) <= 20:
        card_random = [0, 1]
        computer_random = rand.choice(card_random)
        if computer_random == 1:
            computer_card3 = rand.choice(card_choices)
            print("The computer has picked a new card!")
            print("")
        else:
            print("")      
    computer_cards = (computer_card1 + computer_card2 + computer_card3)

# Decides the winner
    if player_cards > 21 and computer_cards > 21:             # IF both player and computer over 21 then no one wins
        print("You both lost!")
        print("Your score was: ", player_cards)
        print("The computer's score was: ", computer_cards)
        print("")
        total_games += 1
    elif player_cards > computer_cards:                       # Checks if the player has a higher card
        if player_cards > 21:                                 # If it is over 21 they lose
            print("You Lose!")
            print("Your score was: ", player_cards)
            print("The computer's score was: ", computer_cards)
            print("")
            computer_score += 1
            total_games += 1

        elif player_cards > 0 and player_cards <= 21:         # If it is between 0 and 21 they win
            print("You Win!!")
            print("Your score was: ", player_cards)
            print("The computer's score was: ", computer_cards)
            print("")
            player_score += 1
            total_games += 1

    elif computer_cards > player_cards:                       # Checks if the computer has a higher card
        if computer_cards > 21:                               # If it is over 21 they lose
            print("You Win!!")
            print("Your score was: ", player_cards)
            print("The computer's score was: ", computer_cards)
            print("")
            player_score += 1
            total_games += 1

        elif computer_cards > 0 and player_cards <= 21:       # If it is between 0 and 21 they win
            print("You Lose!!")
            print("Your score was: ", player_cards)
            print("The computer's score was: ", computer_cards)
            print("")
            computer_score += 1
            total_games += 1

    elif computer_cards == player_cards:                      # If they are the same they tie and no one wins
        print("You tied!!")
        print("Your score was: ", player_cards)
        print("The computer's score was: ", computer_cards)
        print("")
        total_games += 1
        

    reset = input("Would you like to reset? Y or N: ")
    print("")
    if reset == "Y":
        reset = True
    else:
        reset = False
print("You won: ", player_score, " games!")
print("The computer won: ", computer_score, " games!")
print("You played: ", total_games, " games")
print("Goodbye!")