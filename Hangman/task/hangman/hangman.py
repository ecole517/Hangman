import random
word = ['python', 'java', 'kotlin', 'javascript']
msg_1 = 'Input a letter:'
msg_2 = 'That letter doesn\'t appear in the word'
msg_3 = 'Thanks for playing!'
msg_4 = 'We\'ll see how well you did in the next stage'
menu = 'Type \"play\" to play the game,\"exit\" to quit:'
selected_word = random.choice(word)
guesses = 0
a = selected_word
b = list(len(a)*'-')
chosen = []

print("H A N G M A N")
print(menu)
button = input()
if button == 'play':
    print('')
    print(''.join(b))
elif button == 'exit':
    quit()
while True:
    if guesses < 8:
        user_input = input('Input a letter:')
        if len(user_input) > 1:
            print("You should input a single letter")
            print('')
            print(''.join(b))
            continue
        if user_input.isalpha() is False:
            print('Please enter a lowercase English letter')
            print('')
            print(''.join(b))
            continue
        if user_input.isupper():
            print('Please enter a lowercase English letter')
            print('')
            print(''.join(b))
            continue
        if user_input in chosen:
            print('You\'ve already guessed this letter')
            print('')
            print(''.join(b))
            continue
        if user_input in chosen and user_input in a:
            print('No improvements')
            if guesses == 8:
                print('You lost')
                break
        if user_input not in a:
            print(msg_2)
        for i in range(0, len(a)):
            if user_input == a[i]:
                b[i] = user_input
        if user_input in chosen or user_input not in a:
            guesses += 1
            if guesses == 8:
                print('You lost!')
                break
        chosen.append(user_input)
        print('')
        print(''.join(b))
        if (''.join(b)) == a:
            print('You guessed the word!')
            print('You survived!')
            break
    else:
        break
