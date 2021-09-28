import json
import string
import os 
import random
import time 

#this function is to take input of a single character and nothing else
def letterInput():
    guess = ''
    while len(guess) != 1:
        guess = input("Input your guess(must be a single letter): ").lower()
        if not guess.isalpha():
            guess = guess + 'aa'
            print('Please type a letter not a number...')
        elif len(guess) > 1:
            print('Type a single letter not hmm...')

    return guess



if __name__ == '__main__':

    # data = json.load(open("C:/Users/Steinium/Documents/MS code/pyadv/dictionary/dictionary.json", 'r'))
    # WordList = [data[i]["word"].lower() for i in range(len(data)) if (len(data[i]["word"]) >= 5) and (not any(a in list(data[i]["word"]) for a in string.punctuation))]
    
    with open("C:/Users/Steinium/Documents/MS code/pyadv/dictionary/dictionary.json", 'r') as fp:
        data = json.load(fp)
        WordList = [data[i]["word"].lower() for i in range(len(data)) if (len(data[i]["word"]) >= 5) and (not any(a in list(data[i]["word"]) for a in string.punctuation))]


    ThatDictionary = {'7': -21, '6': -9, '5': 1, '4': 7, '3': 19, '2': 26, '1': 38, '0': 49}

    core = 0
    for a in range(1, 11):
        num = random.randint(0,len(WordList))
        word = WordList[num]
        
        structure = ['_' for i in word]
        missed = []
        chance = 0

        print(f'********{a}/10********                    Difficulty: I don\'t know :) ')
        print(' ',*structure,"\n", ' chances left:', (7-chance),f'\t \t \t \tScore: {core}/1000\n')

        while chance <= 7:
            guess = letterInput()
            os.system('cls')
            if (guess in word) and (guess not in structure):
                for num, i in enumerate(word):
                    if i == guess:
                        structure[num] = guess
                missed.append(guess)
            elif ((guess in word) and (guess in structure)) or (guess in missed):
                print('\n Already typed...\n')
            else:  
                missed.append(guess)
                chance += 1 
                varNum = chance if chance <= 7 else 7

            print(f'********{a}/10********                    Difficulty: I don\'t know :) ')
            print(' ',*structure,"\n", ' chances left:', (7-varNum),f'\t \t \t \t Score: {core}/1000\n')
            print('Used Letters: ', *missed)
            
            lost = True
            if '_' not in structure:
                print('\n*************\nYou win\n*************')
                lost = False
                core += (133 + int(ThatDictionary[str(chance)]))
                break

        
        print(f'\nYou lost :( \n\nAnswer is: {word}\n'  if chance == 8 else '')
        core -= (27 + sum([4 for i in structure if i == '_'])) if lost else 0

        time.sleep(3)
        os.system('cls')
    print(f'*******************************\n Your score is : {core}\n*******************************')
    os.system('pause')