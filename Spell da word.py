import time

user_input = str(input('Write a number: '))

# Unit Chart
units = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': ''
}

# Decimal Chart
decimals = {
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}


# The core
def word_speller(split_word):
    output = ''
    split_word = list(str(number))
    number_length = len(split_word)

    if number_length > 1:
        for i in split_word[number_length - 2]:
            output += decimals.get(i, '#') + ' '
        for uni in split_word[1]:
            output += units.get(uni)
    elif number_length == 1:
        for uni in split_word[0]:
            output = units.get(uni)

    # Exceptions with 'teen'
    if split_word == '13':
        output = 'thirteen'
    elif split_word == '12':
        output = 'twelve'
    elif split_word == '11':
        output = 'eleven'
    elif split_word == '14':
        output = 'fourteen'
    elif split_word == '15':
        output = 'fifteen'
    elif split_word == '16':
        output = 'sixteen'
    elif split_word == '17':
        output = 'seventeen'
    elif split_word == '18':
        output = 'eighteen'
    elif split_word == '19':
        output = 'nineteen'
    else:
        pass
    return len(output)


if len(user_input) > 3:
    print('sorry, you can only write two digit numbers')
number = 1
while number <= int(user_input):
    string_number = str(number)
    time.sleep((1 / (12 / word_speller(number))) + 0.3)
    print(number)
    number += 1
