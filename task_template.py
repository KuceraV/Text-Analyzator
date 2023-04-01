'''
projekt_1.py: první projekt do Engeto Online Python Akademie
Textovy_analyzator

author: Vojtech Kucera
email: vojtechkuc@gmail.com
discord: Vojta K.
'''

import pprint

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# registered users
########################################################
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

separator = 40 * '-'
# input of nickname and password
#######################################################
username = input('Insert your username: ')
password = input('Insert your password: ')


# authentication of registered user and valid password
if username in users:

    if users[username] == password:
        print(separator,
              f'Welcome to the app, {username}',
              'We have 3 texts to be analyzed.',
              separator,
              sep='\n')
    else:
        print('password not valid')
        quit()
else:
    print('Unregistered user, terminating the program...')
    quit()

# choice of text to be analyzed
#######################################################
text_choice = (input('Enter a number btw. 1 and 3 to select: '))
text_number = ['1', '2', '3']

# choice of the text has to be digit and in range(1-3)
#######################################################
if not (text_choice.isdigit()) or (text_choice not in text_number):
    print('Insert only integer in range from 1 to 3')
    quit()
else:
    text_choice = int(text_choice)

analyzed_text = TEXTS[text_choice - 1]

# word_list = []
#
# for word in analyzed_text.split():
#     word_list.append(word.strip(',.!?;'))

word_list = [word.strip(',.!?;') for word in analyzed_text.split()]

# pprint.pprint((word_list))

# number of words
#######################################################
word_count = len(word_list)

# sum of all title words
#######################################################
sum_title_words = 0

for title_word in word_list:
    if title_word.istitle():
        sum_title_words += 1

# sum of all upper words
#######################################################
sum_upper_words = 0

for upper_word in word_list:
    if upper_word.isupper() and upper_word.isalpha():
        sum_upper_words += 1

# sum of all lower words
#######################################################
sum_lower_words = 0

for lower_word in word_list:
    if lower_word.islower():
        sum_lower_words += 1

# sum of all numer string
#######################################################
sum_num_str = 0

for num_str in word_list:
    if num_str.isdigit():
        sum_num_str += 1

# sum of string numbers
#######################################################
sum_num_word = 0

for num_str in word_list:
    if num_str.isdigit():
        num_int = (int(num_str))
        sum_num_word += num_int

# print of results
#######################################################
print(
    separator,
    f'There are {word_count} words in the selected text.',
    f'There are {sum_title_words} titlecase words.',
    f'There are {sum_upper_words} uppercase words.',
    f'There are {sum_lower_words} lowercase words.',
    f'There are {sum_num_str} numeric strings.',
    f'The sum of all the numbers {sum_num_word}.',
    sep='\n'
)

print(separator)
print('LEN|', 'OCCURENCE'.center(18), '|NR.')
print(separator)


# calculating the frequency of the words length and print the results
#######################################################
frequency = {}

for len_of_word in word_list:
    if len(len_of_word) not in frequency:
        frequency[len(len_of_word)] = 1
    else:
        frequency[len(len_of_word)] += 1

for key, value in sorted(frequency.items()):
    print(
        str(key).rjust(3) + '|',
        ("*" * value) + '|'.rjust(20 - value),
        value
    )