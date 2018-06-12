class Compiler():
    def __init__(self):
        self.SourceFile = open("D:\\GitHub\\School_Works\\Python\\Principles_of_Compiler\\Letter_Ana\\sample.txt", 'r')
        self.ch = ''
        self.code = 0
        self.flag = 0
        self.flag2 = 0
        self.letter = 0
        self.signal = 0
        self.Line_Count = 0
        self.sign_test_cont = 0
        self.strToken = ''
        self.signToken = ''
        self.retainWord = ["int","if","else","return","main","void","while","break"]
        self.letterSign = ["++","--",">>","<<","+=","-=","*=","/=","&&","||","/*","*/"]

    def IsBC(self,ch):
        if (ch == ' '):
            return True
        return False

    def Reserve(self):
        if self.Error_Report_Str() == 1:
            return 4
        for i in range(0, len(self.retainWord)):
            if self.strToken == self.retainWord[i]:
                return 1
        if len(self.strToken) != 0:
            if self.strToken[0].isdigit:
                return 3
        return 2

    def Retract(self):
        self.code = self.Reserve()
        if self.code == 1:
            print("(" + " 1, " + "' " + self.strToken + " ')")
        elif self.code == 2:
            print("(" + " 2, " + "' " + self.strToken + " ')")
        elif self.code == 3:
            print("(" + " 3, " + "' " + self.strToken + " ')")
        self.strToken = ''
    
    def LetterSign(self):
        for i in range(0, len(self.letterSign)):
            if self.signToken == self.letterSign[i]:
                self.flag = 3
                return 1
        self.sign_test_cont = self.sign_test_cont + 1
        if self.sign_test_cont == 2 and self.flag != 3:
            self.flag = 1
        return 0

    def Retract_Sign(self):
        self.letter = self.LetterSign()
        if self.letter == 1:
            print("(" + " 6, " + "' " + self.signToken + " ')")
            self.signToken = ''

    def Error_Report_Str(self):
        if len(self.strToken) > 1 and self.strToken[0].isdigit():
            for i in range(0, len(self.strToken)):
                if self.strToken[i].isdigit() != 1:
                    print("Syntax Error: In line " + str(self.Line_Count) + "Cannot recognize variable '" + self.strToken + "'")
                    self.strToken = ''
                    self.flag2 = 99
                    return 1
        return 2

    def Error_Report_Sign(self):
        if self.signToken == "&" or self.signToken == "|":
            print("Syntax Error: in line " + str(self.Line_Count) + ": Unrecognized symble decleared '" + self.signToken + "'")
            self.signToken = ''
            self.flag2 = 99
            return 0
        return 2

    def Scanner(self):
        for FileLine in self.SourceFile:
            for ch in FileLine:
                if ch == '\n':
                    self.Line_Count += 1
                if self.IsBC(ch) == False:
                    if ch.isalpha() == True:
                        self.strToken = self.strToken + ch
                    elif ch.isdigit() == True:
                        self.strToken = self.strToken + ch
                    elif ch == '=':
                        if len(self.strToken) != 0 and self.strToken[0] == '=':
                            self.strToken = self.strToken + ch
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.strToken = ''
                        else:
                            self.strToken = self.strToken + ch
                    elif ch == '+':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag == 0
                    elif ch == '*':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == '/':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == ';':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '(':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == ')':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '{':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '}':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == ',':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '!':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '"':
                        self.Retract()
                        print("(" + " 5, " + "' " + ch + " ')")
                    elif ch == '<':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == '>':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == '|':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == '/':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                    elif ch == '&':
                        self.Retract()
                        self.signToken = self.signToken + ch
                        self.Retract_Sign()
                        self.signal = 1
                        self.flag2 = 0
                        if self.flag == 1:
                            print("(" + " 4, " + "' " + ch + " ')")
                            self.flag = 0
                else:
                    self.Retract()
                self.flag2 = self.flag2 + 1
                if self.flag2 == 2 and self.signal == 1 and self.flag != 1 and len(self.signToken) != 0:
                    temp2 = self.Error_Report_Sign()
                    if temp2 == 0:
                        continue
                    print("(" + " 4, " + "' " + self.signToken + " ')")
                    self.signToken = ''
                    self.flag2 = 99
                elif self.flag2 == 2:
                    self.flag2 = 99


if __name__ == '__main__':
    Test = Compiler()
    Test.Scanner()