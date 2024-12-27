""""
Define a function called myfunc that takes in a string, 
and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. 
Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
The output string can start with either an uppercase or lowercase letter, 
so long as letters alternate throughout the string.


"""

def myfunc(MyString):
    NewList = []
    Count = 0
    NewString = ""

    for i in MyString:
        if Count % 2 == 0:
            Temp = i.upper()
            NewList.append(Temp)
            Count += 1

        elif Count % 2 != 0:
            Temp = i.lower()
            NewList.append(Temp)
            Count +=1


    for x in NewList:
        NewString += x


    return NewString

Result = myfunc("james")
print(Result)