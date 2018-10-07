plain_word = "HI"
secret_word = "FORT"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mixed_letters = secret_word
for x in letters:
    if x not in secret_word:
        mixed_letters = mixed_letters + x

print(mixed_letters)
print(letters)

result = ""
for x in plain_word:
    index = letters.index(x)
    result = result + mixed_letters[index]

print(result)
print(plain_word)

    
