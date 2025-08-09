import art
import game_data
import random

print(art.logo)
A = random.choice(game_data.data)
score = 0
done_list=[A]
def higher_lower():
    global A
    global score
    filtered_list = [x for x in game_data.data if x not in done_list]
    B = random.choice(filtered_list)
    done_list.append(B)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    if A['follower_count'] >= B['follower_count'] and guess == 'a':
        score += 1
        print(f"You're right! Current score: {score}.")
    elif B['follower_count'] >= A['follower_count'] and guess == 'b':
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        return
    A = B
    higher_lower()
higher_lower()