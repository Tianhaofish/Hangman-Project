from HangmanModule import *

def get_letter_position(let):
    letter_positions = {}
    let_list = create_letter_list('apple')
    let_list_copy = let_list[:]
    for letter in let_list_copy:
        if letter in let_list:
            index_list = []
            while letter in let_list:
                index = let_list.index(letter)
                index_list.append(index)
                letter_positions[letter] = index_list
                let_list.remove(letter)
                let_list.insert(index, '0')
    a = letter_positions
    b = a[str(let)]

    index_list=[]
    for i in b:
      index_list.append(i)

    #print(index_list)

    return index_list

get_letter_position('p')

def coordinates(let):
    coor={}
    for i in get_letter_position(let):
        coor[let]=500+i*50
    a=coor[let]
    print(a)
    return a
    print(a)
coordinates('a')








