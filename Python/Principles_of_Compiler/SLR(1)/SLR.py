from Gramma2 import GRAMMA, VOL
from Generator import Generator
from copy import deepcopy

class SLR:
    def __init__(self, GRAMMA, VOL):
        self.GRAMMA = GRAMMA
        self.VOL = VOL
        self.Generator = Generator(self.GRAMMA, self.VOL)
        self.Generator.Free_Left_Recursive()
        self.Producer = []
        self.Projects = []
        self.C = [] * 100
        self.ensure = 0
        self.Extand_Seq = ['E_', ['E']]
        #self.Extand_Seq = ['S_', ['S']]
        self.Has_Deri = 0
        self.Generator.First_Gene()
        self.FIRST = self.Generator.first
        self.Generator.Follow_Gene()
        self.FOLLOW = self.Generator.follow
        self.ACTION = {status : { not_end : {} for not_end in self.VOL['T'] } for status in range(0, 1)}
        self.GOTO = {status : { not_end : {} for not_end in self.VOL['N'] } for status in range(0, 1)}
        
    def Create_Producer_Sequence(self):
        self.Producer.append(self.Extand_Seq)
        for key in self.GRAMMA.items():
            for right in self.GRAMMA[key[0]]:
                if right != '|':
                    self.Producer.append([key[0], right])
    
    def insert(self, original, new, pos):
        return original[:pos] + new + original[pos:]

    def Create_Project_Sequence(self):
        counter = 0
        for producer in self.Producer:
            for i in range(0, (len(producer[1]) + 1)):
                self.Projects.append(deepcopy((producer)))
                if isinstance(self.Projects[counter][1], list):
                    self.Projects[counter][1].insert(i, '@')
                else:
                    self.Projects[counter][1] = self.insert(self.Projects[counter][1], '@', i)
                counter = counter + 1
    
    def Is_Derivation(self, pos):
        Derivation_Sequence = []
        for proj in self.C[pos]:
            if proj[1][-1] == '@':
                break
            if proj[1][proj[1].index('@') + 1] in list(set(self.VOL['N'])^set(self.VOL['T'])):
                if proj[1][proj[1].index('@') + 1] in Derivation_Sequence:
                    continue
                Derivation_Sequence.append(proj[1][proj[1].index('@') + 1])
        return Derivation_Sequence

    def GO(self, C, Deri, pos):
        flag = 0
        for c in C:
            if c[1][-1] != '@':
                if Deri in c[1][c[1].index('@') + 1]:
                    flag2 = 0
                    for c2 in self.C:
                        if self.Projects[self.Projects.index(c) + 1] in c2:
                            if Deri in self.VOL['T']:        
                                self.ACTION[self.Has_Deri][Deri] = self.C.index(c2)
                            flag2 = 1
                            break
                    if flag2 == 1:
                        continue    
                    self.C[pos].append(self.Projects[self.Projects.index(c) + 1])
                    if Deri in self.VOL['N']:
                        self.GOTO[self.Has_Deri][Deri] = pos
                    if Deri in self.VOL['T']:        
                        self.ACTION[self.Has_Deri][Deri] = pos
                    flag = 1
        if pos != self.C.index(self.C[pos]):
            self.C[pos] = []
        if flag == 1:
            return 1

    def Is_In_C(self, i):
        for c in self.C:
            if self.C[i] == c and self.C.index(c) != i:
                return self.C.index(c)
            else:
                return False

    def Closure(self, i):
        Derivation_Sequence = self.Is_Derivation(i)
        if len(Derivation_Sequence) != 0:
            self.Has_Deri = i
            for deri in Derivation_Sequence:
                for proj in self.Projects:
                    if deri in proj and proj[1][0] == '@' and proj not in self.C[i]:
                        self.C[i].append(proj)

    def Create_C_Sequence(self):
        i = 0
        ensure = 0
        temp = 0
        Derivation_Sequence = []
        self.C.append([self.Projects[0]])
        while True:
            old_C_all = deepcopy(self.C)
            if i == 1:
                self.C.append([])
            while True:
                old_C = deepcopy(self.C)
                if i == 0:
                    Derivation_Sequence = self.Is_Derivation(0)
                else:
                    temp = self.C.index(self.C[-1])
                    for Deri in Derivation_Sequence:
                        is_append = self.GO(self.C[self.Has_Deri], Deri, temp)
                        self.Closure(temp)
                        if is_append == 1:
                            self.C.append([])
                            self.GOTO_ADD(temp)
                            self.ACTION_ADD(temp)
                            temp = temp + 1
                    Derivation_Sequence = self.Is_Derivation(i)
                if len(Derivation_Sequence) != 0:
                    self.Has_Deri = i
                    for deri in Derivation_Sequence:
                        for proj in self.Projects:
                            if deri in proj and proj[1][0] == '@' and proj not in self.C[i]:
                                self.C[i].append(proj)
                if old_C == self.C :
                    if ensure == 0:
                        ensure = 1
                        continue
                    else:
                        ensure = 0
                    break
#            for temp in self.C[i]:
#                print(temp)
            i = i + 1
            if old_C_all == self.C and self.C.index(self.C[-1]) == i:
                del self.C[-1]
                for item, j in zip(self.C, range(0, len(self.C))):
                    for sub_item in item:
                        if sub_item[1][-1] == '@':
                            producer = deepcopy(sub_item)
                            producer[1] = producer[1][:-1]
                            recursive = 'r' + str(self.Producer.index(producer))
                            if sub_item[1][0] == 'E':
                            #if item[0][1][-2] == '#':
                                self.ACTION[j]['#'] = 'acc'
                                continue
                            for Deri in self.VOL['T']:
                                if Deri not in self.FOLLOW[sub_item[0]]:
                                    continue
                                if self.ACTION[j][Deri] != {}:
                                    self.ACTION[j][Deri] = str(self.ACTION[j][Deri]) + ',' + recursive
                                    continue
                                self.ACTION[j][Deri] = recursive
                break

    def GOTO_ADD(self, status):
        self.GOTO[status] = { not_end : {} for not_end in self.VOL['N'] }

    def ACTION_ADD(self, status):
        self.ACTION[status] = { not_end : {} for not_end in self.VOL['T'] }

    def Form_Display(self):
        print("nothing")

if __name__ == '__main__':
    test = SLR(GRAMMA, VOL)
    test.Create_Producer_Sequence()
    test.Create_Project_Sequence()
    test.Create_C_Sequence()
    for c, i in zip(test.C, range(0, len(test.C))):
        print(str(i) + ' : ' + str(c))

        
