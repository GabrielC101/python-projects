#!/usr/bin/env python

import argparse

def isVowel(string):
    if string.upper() in 'AEIOU':
        return True
    else:
        return False

def countVowels(string):
    vowel_dict = {'A':0,'E':0,'I':0,'O':0,'U':0}
    for s in string:
        if isVowel(s):
            vowel_dict[s.upper()] = vowel_dict[s.upper()] + 1
    return vowel_dict



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="word to have vowels counted", action="store", nargs="*")


    args = parser.parse_args()

    if args.word:
        a = args.word
    else:
        a = "Hello World!"

    #print "For " + a + ", the spread is:"

    for s in a:
        vowel_dict = countVowels(s)
        print "For " + s + ", the spread is:"
        print 'A :' + str(vowel_dict['A'])
        print 'I :' + str(vowel_dict['I'])
        print 'O :' + str(vowel_dict['O'])
        print 'E :' + str(vowel_dict['E'])
        print 'U :' + str(vowel_dict['U'])
        print '-----------------------------'