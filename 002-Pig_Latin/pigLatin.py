#!/usr/bin/env python


def isVowel(string):
    if string in 'aeiouAEIOU':
        return True
    else:
        return False

def getFirstLetter(string):
    return string[0]

def translateWord(string):
    if ' ' in string:
        raise ValueError("This function only translates one word at a time. This string contains a space.")

    first_letter = getFirstLetter(string)
    first_letter_is_vowel = isVowel(first_letter)

    if first_letter_is_vowel:
        return string + """'way"""
    else:
        return string[1:] + """'""" + first_letter + "ay"

















if __name__ == "__main__":
    word_list = ['hello','paytime', 'OK', 'alphabet', 'time',]

    for w in word_list:
        pig_latin_word = translateWord(w)
        print pig_latin_word