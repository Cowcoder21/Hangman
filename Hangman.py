#!/usr/bin/env python
# coding: utf-8

# In[84]:



def guess():
    target = input("The word the others have to guess is: "  )
    letters = 'abcdefghijklmnopqrstuvwxyz'
    max_attempts = 3
    counter = 0
    previous_guesses = []
    while True:
        guess = input ("Guess a letter in the target word: ")
        if guess not in letters:
            print("Chose another character which is a letter")
            continue
        elif guess in previous_guesses:
            print("You have already guessed this letter, try another ")
            continue
        elif guess not in target:
                counter += 1
                print("thats a strike! Only " + str(max_attempts - counter) + " guesses left! keep going")
                print (counter)
                previous_guesses.append(guess)
                if counter == max_attempts:
                    print("You are out of guesses!")
                    break
        elif guess in target:
            print("You got a correct guess! keep going")
            target = target.replace(guess, "")
#             print(target)
            previous_guesses.append(guess)
            if target == "":
                print("You have guessed the word! you win!")
                break
            else:
                continue
        elif guess in previous_guesses:
            print("You have already guessed this letter ")
            continue

           
            
        

print (guess())

    


# In[ ]:





# In[ ]:





# In[ ]:




