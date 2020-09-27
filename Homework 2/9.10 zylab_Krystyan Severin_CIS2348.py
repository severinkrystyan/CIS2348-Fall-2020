"""Name: Krystyan Severin
   PSID: 1916594"""
import csv
word_list = []  # Stores word list from input file
freq_list = []  # Stores words and their frequencies
file_name = input()
with open(file_name) as file:
    words = csv.reader(file)
    for x in words:
        word_list.extend(x)
    file.close()
for idx, word in enumerate(word_list):
    found = False  # Determines if word is already in frequency list
    for i, _ in enumerate(freq_list):
        if word == freq_list[i][0]:
            freq_list[i][1] += 1
            found = True
    if not found:
        freq_list.append([word, 1])
for i, _ in enumerate(freq_list):
    print(f'{freq_list[i][0]} {freq_list[i][1]}')
