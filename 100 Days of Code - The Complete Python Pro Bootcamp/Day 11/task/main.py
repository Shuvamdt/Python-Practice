import random
import art
cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def ace_check(game_cards):
    while 11 in game_cards and sum(game_cards)>21:
        game_cards.remove(11)
        game_cards.append(1)
    return game_cards

def blackjack():
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == "n":
        return
    print(art.logo)
    your_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    your_cards=ace_check(your_cards)
    computer_cards=ace_check(computer_cards)
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while hit == "y":
        your_cards.append(random.choice(cards))
        your_cards=ace_check(your_cards)
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if sum(your_cards)>21:
            break
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    while sum(computer_cards)<16 and sum(your_cards)<21:
        computer_cards.append(random.choice(cards))
        computer_cards=ace_check(computer_cards)
    print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    if sum(your_cards) > 21:
        print("You went over. You lose 😭")
    elif sum(your_cards) > sum(computer_cards):
        print("You win 😃")
    elif sum(your_cards) == sum(computer_cards):
        print("Its a draw")
    elif sum(computer_cards) > 21:
        print("Opponent went over. You win 😁")
    else:
        print("You lose 😤")
    print("\n"*20)
    blackjack()

blackjack()