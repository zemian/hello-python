#Ask user to enter a word.
#Reverse the order of all the letters in this word
#Print the result
#
#This program was created by Kenny on 9\17\17
#
word = input("Please enter a word")
word_length = len(word)
for k in (range(word_length - 1, -1, -1)):
    print(word[k])
