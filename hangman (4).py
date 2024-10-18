
print('hello welcome. Hope you ready for the game')
import random

my_file = open("C:/Users/N1102393/Downloads/wordlist.txt", "r")

word = my_file.readlines()

choose_word =  random.choice(word)
choose_word = choose_word.lower()
print( choose_word) 
def user_input():
    
    len_of_word = len(choose_word)
    print(f'Hint! the number of letter in for your guessing world is {len_of_word}')
    
    correct_guessed = 0
    guessed_letter = []
    num_of_try = 4
    word_dash =  ['_']*len(choose_word)
    print('Let get started')
    print(word_dash)

    while correct_guessed <len(choose_word) and num_of_try > 0:
        guessed = False
        # give the player instruction for inputing in lower case
        player = input('Guess a letter? ')
        

        if player.isalpha() and len(player) ==1:
            if player in guessed_letter:
                num_of_try -=1 
            
                print(f'it been guessed try again. Number of life is {num_of_try}')
                if num_of_try == 0:
                    print('You lose!')


            elif player not in choose_word:
                
                num_of_try -= 1
                
                if num_of_try == 0:
                    print('You exorted your life trail. You lose! ')
                print(word_dash)
        # add a csv files
        #we can also use pickles if you dont want to write``
                    
                print(f'the letter is not in the word. You have {num_of_try} lives left.')
                
                
            else:
                guessed_letter.append(player)
                for i in range(len(choose_word)):
                    if player == choose_word[i]:
                        word_dash[i] = player
                        guessed = True
                        correct_guessed += 1
                        
                        len_of_word -= 1
                print('Current word:', ''.join(word_dash))
                print(f'Number of letter remain is {len_of_word} ')
                print(guessed_letter)
                print(word_dash)
                if correct_guessed == len_of_word:
                    print('You won, GOod job!')
                    break
                

                
result2 = user_input()
print(result2)               
               


      




    


    
    
    
