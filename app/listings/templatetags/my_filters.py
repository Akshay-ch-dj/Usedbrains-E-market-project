from django import template

register = template.Library()


def rupeeCommaInsert(num):
    myList = list(str(num))
    i = len(myList) - 3

    while(i > 0):
        myList.insert(i, ',')
        i -= 2

    return ''.join(myList)


def charLimitter(str):
    limit = 20
    return str[0:limit+1]


register.filter('insertComma', rupeeCommaInsert)
register.filter('charLimitter', charLimitter)
