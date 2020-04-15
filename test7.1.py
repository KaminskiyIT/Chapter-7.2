#! python3
# test7.1 - функция, которая использует регулярные выражения для проверки того,
# что переданная ей строка представляет собой сильный пароль.
# Сильными считаются пароли, которые состоят по крайней мере из восьми символов,
# содержат символы в верхнем и нижнем регистрах и включают по крайней мере одну цифру.

import re

def coolPassword():
    while True:
        print('Enter your password:')
        myPassword = input()
        if len(myPassword) >= 8:
            passwordNumberRegex = re.compile(r'[0-9]+')
            passwordLowerWordsRegex = re.compile(r'[a-z]+')
            passwordHigherWordsRegex = re.compile(r'[A-Z]+')
        
            if passwordNumberRegex.search(myPassword) != None:
                if passwordLowerWordsRegex.search(myPassword) != None:
                    if passwordHigherWordsRegex.search(myPassword) != None:
                        print('Strong password!')
                        break
    
        else:
            print('Weak password.\nThe minimum password length is 8 characters!')
            continue
        print('Weak password!')

coolPassword()
