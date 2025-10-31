import random


words = {"shiraz" :["it is a city in iran", "It is widely known as the Iranian city of Poets, Literature, and Gardens.",
        "The city is home to the greatest poets, Hafez and Saadi"] ,"tabriz":["the capital of Iran several times throughout history.","World Carpet Weaving City","cultural center of East Azerbaijan Province"],
         "isfehan":["It was the capital of Persia during the Safavid dynasty.","Naghsh-e Jahan"]}
word = random.choice(list(words.keys()))
hints = words[word].copy()
current_guess = ["_" for _ in word]
attempts = 10

n_hint = (len(hints))
while attempts > 0 and "_" in current_guess:
    print("Word:", " ".join(current_guess))
    guess = input("Enter your guess: ")
    
    if guess in word:
        found = False
        for i in range(len(word)):
            if word[i] == guess:
                current_guess[i] = guess
                found = True
        if found:
            print("Correct guess!")
            print("_"*10)
            
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left")
        print(f'you have {n_hint} hints left')
        print("_"*10)
        hint_input = input("do you want a hint? (y/n)")
        if hint_input == "y":
            if n_hint > 0:
                print("^" *15)
                print(hints[random.randint(0, n_hint - 1)])
                print("^" *15)
                
                n_hint -= 1
            else:
                print("You have no hints left")
                break

        
if "_" not in current_guess:
    print("*" * 10)
    print("Congratulations! You win!")
    print("The word was:", word)
else:
    print("*" * 10)
    print("Game over! You lose!")
    print("The word was:", word)