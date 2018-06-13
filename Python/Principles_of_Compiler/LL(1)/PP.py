'''
    Author : Lin Zipeng
    Stu.num : 15281266
    School : Beijing Jiaotong University
    Prof : Computer Science & Technology
    Function : Predication Parsing on LL(1)
'''

from Gramma import ANNA_TABLE, GRAMMA, VOL
from Stack import Stack

string = ''
string_counter = 0
anna_stack = Stack()
pop = ''
flag_syn = 0
flag_char = 0
curr_stor = 0

def Predication_Parsing():
    global string
    global pop
    global anna_stack
    global string_counter
    string = '(i+i)#'
    anna_stack.push('#')
    result = Predication('E')
    if result == 1:
        print ("This is a right string!")
    elif flag_char == 1:
        print("Unknown charactor near '" + string[:curr_stor]  + "' Please check your string!")
    elif flag_syn == 1:
        print("Syntax error near '" + string[:curr_stor] + "' Please check your string!")

def Predication(CANDI):
    global flag_syn
    global flag_char
    global string_counter
    global anna_stack
    global current
    global curr_stor
    current = string[string_counter]
    while(1):
        if flag_char == 1:
            return 0
        if CANDI == 'E' and 'E' not in ANNA_TABLE[current] or flag_syn == 1:
            return 0
        elif anna_stack.peek() == '#' or string_counter != len(string):
            if CANDI != 'e':
                for non_end in reversed(CANDI):
                    if non_end in anna_stack.peek():
                        continue
                    anna_stack.push(non_end)
            if anna_stack.peek() in VOL['T']:
                if anna_stack.peek() == current:
                    string_counter = string_counter + 1
                    #print (anna_stack.disp())
                    anna_stack.pop()
                    current = string[string_counter]
                    if current not in VOL['T']:
                        curr_stor = string.index(current)
                        flag_char = 1
                        return 0
                    return 1
                else:
                    return 0
            if anna_stack.peek() != '#':
                pop = anna_stack.pop()
                if pop not in ANNA_TABLE[current]:
                        return 0
                if Predication(ANNA_TABLE[current][pop]):
                    if anna_stack.peek() == '#' and current == '#':
                        return 1
                    if anna_stack.peek() not in ANNA_TABLE[current]:
                        return 0
                    if ANNA_TABLE[current][anna_stack.peek()] == 'e':
                        while ANNA_TABLE[current][anna_stack.peek()] == 'e' and anna_stack.peek() != '#':
                            anna_stack.pop()
                            if anna_stack.peek() in ANNA_TABLE[current]:
                                CANDI = ANNA_TABLE[current][anna_stack.peek()]
                            else:
                                break
                        if anna_stack.peek() == '#' and current == '#':
                            return 1
                
                    else:
                        pop = anna_stack.pop()
                        CANDI = ANNA_TABLE[current][pop]
                    if anna_stack.peek() == '#' and current != '#':
                        curr_stor = string.index(current)
                        flag_syn = 1
                        return 0
                    if anna_stack.peek() != '#' and current == '#':
                        curr_stor = string.index(current)
                        flag_syn = 1
                        return 0
        else:
            return 1
                

Predication_Parsing()