import random
pictures = [
" +----\n"
"     |\n"
"     |\n"
"     |\n"
"     |\n",

" +----\n"
" O   |\n"
"     |\n"
"     |\n"
"     |\n",

" +----\n"
" O   |\n"
" +   |\n"
"     |\n"
"     |\n",

" +----\n"
" O   |\n"
"-+   |\n"
"     |\n"
"     |\n",

" +----\n"
" O   |\n"
"-+-  |\n"
"     |\n"
"     |\n",

" +----\n"
" O   |\n"
"-+-  |\n"
" |   |\n"
"     |\n",

" +----\n"
" O   |\n"
"-+-  |\n"
" |   |\n"
"/    |\n",

" +----\n"
" O   |\n"
"-+-  |\n"
" |   |\n"
"/ \  |\n"
]

word_list = ['HELLO', 'PYTHON', 'FUN', 'COLOR', 'MINECRAFT']
selected_word = word_list[random.randint(0, len(word_list)) - 1]
guess_letters = []
for _ in range(len(selected_word)):
    guess_letters.append('_')
max_guess = len(pictures)
incorrect_guess_count = 0
finish = False
print('Welcome to hangman game.')
while not finish:
    print('Word: ' + ' '.join(guess_letters))
    
    letter = input('Guess a letter: ')
    
    if not letter.isalpha():
        print('You did not enter a letter, try again.')
        continue

    # Check letter against selected_word
    letter = letter.upper()
    guess_correct = False
    for i in range(len(selected_word)):
        if letter == selected_word[i]:
            guess_correct = True
            guess_letters[i] = letter

    if ''.join(guess_letters) == selected_word:
        print('You won!')
        break
    
    if guess_correct:
        print('You guessed correct!')
    else:
        print('Incorrect guess. You are about to be hanged!')
        print(pictures[incorrect_guess_count])
        incorrect_guess_count +=1
    
    if incorrect_guess_count >= max_guess:
        print('Game Over: Sorry you have used all your chances!')
        break
    
print(f'The secret word is {selected_word}')
