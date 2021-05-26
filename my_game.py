word="Secreate"
allowed_error=6
guesses=[]
done=False
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("-",end=" ")
            # print("")
    guess=input(f"Allowed errors left{allowed_error},next guess")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
       allowed_error-=1
    if allowed_error==0:
        break
    done = True
    for letter in word.lower():
        if letter.lower() not in guesses:
            done=False

if done:
    print(f"Congratultions! You have found the word it was {word}!")
else:
    print(f"Game over. The world was  {word}!")