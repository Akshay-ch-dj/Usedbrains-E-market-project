from django import template

register = template.Library()


def rupeeCommaInsert(num):
    myList = list(str(num))
    i = len(myList) - 3

    while(i > 0):
        myList.insert(i, ',')
        i -= 2

    return ''.join(myList)


register.filter('insertComma', rupeeCommaInsert)
