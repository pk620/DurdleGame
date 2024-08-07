import random
with open('words.txt', 'r') as file:
    words_list = [line.strip() for line in file]

target = random.choice(words_list)
def durdle_check(guess, target):
    total = ''
    if guess == target:
        return '🟩🟩🟩🟩🟩'
    else:
        for i in range(len(target)):
            if guess[i] not in target:
                total = total + '⬛️'
            elif guess[i] == target[i]:
                total = total + '🟩'
            elif guess[i] in target and guess[i] != target[i]:
                total = total + '🟨'
    return total


def durdle_game(target):
    print('Welcome to Durdle!')
    guess = input('Enter a guess:')
    result = durdle_check(guess, target)
    print(result)
    total = 0
    while guess != target:
        guess = input('Enter a guess:')
        result = durdle_check(guess, target)
        print(result)
        total += 1
        if total > 9 and (total % 5 == 0):
            userDecision = input("Would you like to give up? ")
            if userDecision == "Yes":
                print(target)
    else:
        total += 1
        print('Congratulations, you got it in ' + str(total) + ' guesses!')
    return total
        
if __name__ == '__main__':
    print(durdle_game(target))


        
