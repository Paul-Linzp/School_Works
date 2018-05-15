'''
    Author : Lin Zipeng
    Stu.num : 15281266
    School : Beijing Jiaotong University
    Prof : Computer Science & Technology
    Function : Recursive_Descent_Parsing on LL(1)
'''

'''
    To input the Gramma from Gramma.py
    FIRST : The first set of the gramma
    FOLLOW : The follow set of the gramma
    GRAMMA : The gramma of the language
    VOL : The Vt & Vn set of the gramma
'''
from Gramma import FIRST, FOLLOW, GRAMMA, VOL

#================Variable for analysing================
string = ''   #variable to store the input string
string_counter = 0    #counter for getting the current string index
wrong_char = ''    #signal for wrong string that store the index of wrong string
current = ''    #variable that store the current string token 
para_rec = 0
#=================Recursion Code====================
'''
    Function name : Recursive_Descent_Parsing
    Usage : The entrance of the parsing and display the final result and error report
    Parameter : None
'''
def Recursive_Descent_Parsing():
    global string
    
    string = "i)#" #The input string
    
    result = Recursion('E') #E is the starting charactor of the languange, the function will return whether the string is true of false
    
    if result == 1 and current == '#':
        print ("This is a right string!\n")
    else:
        if result == 1 and current != '#':
            wrong_char = string.index(current)
            print("Unexpected end of string near '" + string[:wrong_char] + "' please check your input!")
        elif string[wrong_char] == '#':
            print("Unexpected end of string near '" + string[:wrong_char] + "' please check your input!")
        elif string[wrong_char] in VOL['T']:
             print("Syntax Error near '" + string[:wrong_char] +"' please check your input!")
        else:
            print("Invalid charactor near '" + string[:wrong_char] +"' please check your input!")

'''
    Function name : Recursion
    Usage : Recursion analysis of the string
    Parameter : None ending Vn token
'''

def Recursion(NONE_ENDING):
    global current #To declare the 'current' will be modified as a global variable
    global wrong_char #The same as current
    if '|' in GRAMMA[NONE_ENDING]: #If there is a '|', there have multiple candidate to be check
        current = string[string_counter] #To get the current token
        if current in FIRST[NONE_ENDING]: #To check if the current token is in the FIRST set
                                          #If true then go to furthor comfirmation
            if current in GRAMMA[NONE_ENDING]: #To justify that if there is a Vt in the candidate set of this Vn
                Advance() #If true then the current advance
                return 1
            else:
                for waiting in GRAMMA[NONE_ENDING]: # Start to check the candidate set
                    if waiting == '|' or waiting in VOL['T'] or waiting == 'e': #Pass the data that has no Vn
                        continue
                    for token in waiting: #The 'token' is the current token of the candidate, e.g. F->(E), then '(' is the first token
                        if token in VOL['T'] and current == token: #If the Vt in the candidate is equal to present current then advance
                            Advance()
                            continue
                        if token in VOL['T'] and current != token:
                            return 0
                        if Recursion(token) == 1: #If the current is the Vn then go Recursion
                            continue
                        elif Recursion(token) == 0 and waiting != GRAMMA[NONE_ENDING][-1]: #If false continue if the current candidate is not the last one
                            continue
                        else:
                            #print("Syntax Error! Unreadable charactor '" + current +"' please check your input!\n")
                            wrong_char = string.index(current)
                            return 0
                #return 1
        elif current in FOLLOW[NONE_ENDING] and 'e' in GRAMMA[NONE_ENDING]: #'e' is epsino, the rule with this can return true if the current isn't in the FIRST set
            return 1
        else:
            return 0
    else:
        current = string[string_counter]
        if current in FIRST[NONE_ENDING]:
            for token in GRAMMA[NONE_ENDING]:
                if token in VOL['T']:
                    continue
                if Recursion(token) == 1:
                    continue
                else:
                    #print("Syntax Error! Unreadable charactor '" + current +"' please check your input!\n")
                    wrong_char = string.index(current)
                    return 0
            return 1
        elif current in FOLLOW[NONE_ENDING] and 'e' in GRAMMA[NONE_ENDING]:
            return 1

'''
    Function name : Advance
    Usage : Move to the next string token until the last one
    Parameter : None
'''
            
def Advance():
    global string_counter
    if (string_counter != len(string)):
        string_counter = string_counter + 1
#===================================================



Recursive_Descent_Parsing()