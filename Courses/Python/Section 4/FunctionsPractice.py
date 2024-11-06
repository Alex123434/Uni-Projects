"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd
"""

def lesser_of_two_evens(a,b):

    Greater = 0
    Smaller = 0

    if a > b:
        Greater = a
        Smaller = b
    else:
        Greater = b
        Smaller = a

    if a % 2 == 0 and b % 2 == 0:
        print(Smaller)
        return Smaller
    
    elif a % 2 != 0 or b % 2 != 0:
        print(Greater)
        return Greater
    
Output = lesser_of_two_evens(2,5)

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns 
True if both words begin with same letter
"""

def animal_crackers(text):
    Temp = []

    MyList = text.split()

    for i in MyList:
        Temp.append(i[0])
    
    LetterOne = Temp[0]
    LetterTwo = Temp[1]

    if LetterOne == LetterTwo:
        print(True)
        return True
    else:
        print(False)
        return False

Output = animal_crackers('Levelheaded Llama')

"""
MAKES TWENTY: Given two integers, 
return True if the sum of the integers is 20 or if one of the integers is 20. 
If not, return False
"""

def makes_twenty(n1,n2):
    Sum = sum([n1,n2])

    if Sum == 20 or n1 == 20 or n2 == 20:
        print(True)
        return True
    else:
        print(False)
        return False

Output = makes_twenty(20,10)

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""

def old_macdonald(name):
    NewNameList = []
    Count = 0

    for i in name:
        if Count == 0 or Count == 3:
            Letter = i.upper()
            NewNameList.append(Letter)
            Count += 1
        else:
            NonCapLetter = i
            NewNameList.append(NonCapLetter)
            Count += 1

    NewName = "".join(NewNameList)

    print(NewName)


Output = old_macdonald('macdonald')
Output = old_macdonald('alex')
Output = old_macdonald('alvarez')