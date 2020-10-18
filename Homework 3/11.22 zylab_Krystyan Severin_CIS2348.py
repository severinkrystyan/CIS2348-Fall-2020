"""Name: Krystyan Severin
   PSID: 1916594"""
words = input().split()  # Creates list with words separated
for x in words:
    print(x, words.count(x))  # Outputs the word along with the amount of times it appears in list
