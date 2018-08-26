def sumuj(argumenty):
    print(argumenty)
    return sum(argumenty)


def sumuj2(*argumenty):
    print(argumenty)
    return sum(argumenty)


def zlacz_teksty (*teksty):
    out = ""
    for teksty in teksty:
        out += teksty
        return out


def dummy (a,b, c=1,d=2,*arga, **kwarga)




#
# argumenty = (1,2,3,4)
#
#
# print(zlacz_teksty('Ala ma kota', ='a'))
#
# print(sumuj(argumenty))
#
# print(sumuj2(1,2,3,4,5,6,7))
#

7