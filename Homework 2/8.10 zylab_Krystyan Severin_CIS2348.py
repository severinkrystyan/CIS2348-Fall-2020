"""Name: Krystyan Severin
   PSID: 1916594"""

word = input()
new_word = word.replace(' ', '')  # Removes white spaces
if new_word[::-1] == new_word:  # Compares reversed word vs initial word
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')
