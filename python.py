#

def has_capital_letter(letter):
    letter = letter[0].isupper()
    return letter

def is_correct_password(password):
   length = len(password)
   return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty1234'))
print(is_correct_password('qwerty1234'))
print(is_correct_password('Qwe1234'))

#

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(not is_even(10))

#

def is_palindrome(text):
    text_lower = text.lower()
    return text_lower == text_lower[::-1]

def is_not_palindrome(text):
    return not is_palindrome(text)

text = 'Salas'
print(is_palindrome(text))
print(is_not_palindrome(text))

#

def guess_number(value):
    given_value = 42
    if value == given_value:
        return 'You win!'
    return 'Try again!'
print(guess_number(42))

#

def normalize_urlq(adress):
    if adress[0:7] == 'http://':
        return 'https://' + adress[6:]
    else:
        return 'https://' + adress

#

def who_is_this_house_to_starks(number):
    match number:
        case 1:
             return 'Tully'
        case 2:
             return 'Frey'
        case _:
             return None
print(who_is_this_house_to_starks(1))

#

def print_numbers(last_number):
    i = last_number
    while i != 0:
        print(i)
        i -= 1
    print('finally')
print(print_numbers(5))

#

def multiply_numbers_from_range(start, stop):
    i = start
    mult = 1
    while i <= stop:
        mult = mult * i
        i = i + 1
    return mult
print(multiply_numbers_from_range(2, 4))

#

def join_numbers_from_range(start, stop):
    i = start
    result = ''
    while i <= stop:
        result = result + str(i)
        i += 1
    return result
print(join_numbers_from_range(1, 5))

#

def print_reversed_word_by_symbol(word):
    i = 0
    word = word[::-1]
    while i < len(word):
        print(word[i])
        i += 1
word = 'hexlet'
print_reversed_word_by_symbol(word)

#

def count_chars(string, char):
    index = 0
    count = 0
    string = string.lower()
    char = char.lower()
    while index < len(string):
        if string[index] == char:
           count = count + 1
        index = index + 1
    return count
print(count_chars('hexlEt', 'e'))

#

def my_substr(string, length):
    i = 0
    result_string = ''
    while i <= length:
        result_string = result_string + string[i]
        i += 1
    return result_string
print(my_substr('areg', 2))

#

def is_arguments_for_substr_correct(string, start, stop):
    if start > stop:
        return False
    elif start < 0:
        return False
    elif stop < 0:
        return False
    elif start + stop > len(string):
        return False
    else:
        return True
print(is_arguments_for_substr_correct('areg',0, 3))

#

def remove_digits(text):
    i = 0
    digits = '0123456789'
    no_digits = ''
    while i < len(text):
        symbol = text[i]
        if symbol not in digits:
            no_digits += symbol
        i += 1
    return no_digits
print(remove_digits('SSkdcjd2333'))

#

def extract_numbers(text):
    i = 0
    numbers = ""
    while i < len(text):
        new_numbers = text[i]
        if new_numbers.isdigit():
            numbers += new_numbers
        i += 1
    return numbers






