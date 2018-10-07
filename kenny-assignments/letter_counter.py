#1. Ask user to enter a sentence.
#2. Then count the number of words you find in the sentence. (Hint: words in a sentence should be separated by a space.)
#3. Print the count result
#
# Created by Kenny Deng 9/16/2017
#
sentence = input("Please enter a sentence ")
len_of_sentence = len(sentence)
words_count = 0
for i in range(len_of_sentence):
    if sentence[i] == ' ':
        words_count += 1
words_count += 1
print(f"you typed {words_count} words!")
