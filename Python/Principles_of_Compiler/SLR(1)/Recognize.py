from Gramma2 import GRAMMA, VOL
from SLR import SLR

class Recognize:
    def __init__(self):
        self.Chara_Stack = []
        self.Input = []
        self.status = []
        self.action = []
        self.GRAMMA = GRAMMA
        self.VOL = VOL
        self.slr = SLR(GRAMMA, VOL)
        self.slr.CREATE_FOLLOW()
        self.slr.Create_Producer_Sequence()
        self.slr.Create_Project_Sequence()
        self.slr.Create_C_Sequence()

    def Get_Input(self):
        In = ['i', '=', 'i', '+', 'i', '*', 'i', '#']
        self.Input = In

    def Scan(self):
        for key in self.GRAMMA.keys():
            for right in self.GRAMMA[key]:
                waiting = self.Chara_Stack[-3:]
                if waiting == right:
                    for i in range(0, 3):
                        del self.status[self.status.index(self.status[-2])]
                        del self.Chara_Stack[self.Chara_Stack.index(self.Chara_Stack[-1])]
                    self.Chara_Stack.append(key)

    def Analyze(self):
        self.status.append('0')
        self.Chara_Stack.append('#')
        for input_chara in self.Input:
            while True:
                if input_chara == '#' and self.Chara_Stack[-1] in self.VOL['N']:
                    self.Scan()
                if self.slr.ACTION[int(self.status[-1])][input_chara] != {}:
                    self.action.append(str(self.slr.ACTION[int(self.status[-1])][input_chara]))
                else:
                    print("ERROR")
                    return 0
                if (self.action[-1].isdigit()):
                    self.status.append(self.action[-1])
                    self.Chara_Stack.append(input_chara)
                    break
                else:
                    self.status.pop()
                    self.Chara_Stack.pop()
                    self.GOTO(int(self.status[-1]), self.slr.Producer[int(self.action[-1][1:])][0])

    def GOTO(self, status, chara):
        if self.slr.GOTO[status][chara] != {}:
            self.status.append(str(self.slr.GOTO[status][chara]))
        else:
            print("ERROR")
            return 0
        self.Chara_Stack.append(chara)


if __name__ == '__main__':
    test = Recognize()
    test.Get_Input()
    test.Analyze()