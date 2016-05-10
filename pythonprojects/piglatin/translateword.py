#!/usr/bin/env python
from getfirstletter import getFirstLetter
from is_vowel import isVowel



def translateWord(string):
    if ' ' in string:
        raise ValueError("This function only translates one word at a time. This string contains a space.")

    first_letter = getFirstLetter(string)
    first_letter_is_vowel = isVowel(first_letter)

    if first_letter_is_vowel:
        return string + """'way"""
    else:
        return string[1:] + """'""" + first_letter + "ay"
