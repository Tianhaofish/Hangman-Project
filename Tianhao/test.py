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


    b=a[str(let)]
    print(b)
    return b

get_letter_position('p')



def cor(let):
    a=get_letter_position(let)
    b=a



#cor('p')



def pp(let):
  a=cor(let)

#pp('p')




