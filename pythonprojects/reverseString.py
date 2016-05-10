#!/usr/bin/env python


def methodOne(string):

    result = string[::-1]

    return result


def methodTwo(string):

    result_list = []
    for s in string:
        result_list.insert(0,s)


    result_string = ''
    for r in result_list:
        result_string = result_string + r


    return result_string







if __name__ == "__main__":
    string = "Hello"

    one = methodOne(string)
    two = methodTwo(string)

    print "Result of methodOne is " + one
    print "Result of methodTwo is " + two

    if one == two:
        print "The results of methodOne and methodTwo are identical."
    else:
        print "There's a problem. The results don't match!"