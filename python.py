def has_capital_letter(letter):
    letter = letter[0].isupper()
    return letter

def is_correct_password(password):
   length = len(password)
   return length > 8 and has_capital_letter(password)

print(is_correct_password('Qwerty1234'))
print(is_correct_password('qwerty1234'))
print(is_correct_password('Qwe1234'))