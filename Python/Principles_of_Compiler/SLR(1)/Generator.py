from Gramma2 import GRAMMA, VOL
from copy import deepcopy

class Generator:
    def __init__(self, GRAMMA, VOL):
        self.GRAMMA = GRAMMA
        self.VOL = VOL
        self.leftpart = GRAMMA.keys()
        self.first = {not_end : [] for not_end in self.leftpart}
        self.follow = {not_end : [] for not_end in self.leftpart}
        self.first_first = set()
        self.real_not_end = ''

    def Find_First(self, not_end):
        not_search_flag = 0
        for right in self.GRAMMA[not_end]:
            if right != 'e' and right[0] in self.VOL['T'] and not_search_flag == 0:
                if right[0] not in self.first[self.real_not_end]:
                    self.first[self.real_not_end].append(right[0])
                    not_search_flag = 1
            elif right[0] in self.VOL['N']:
                self.Find_First(right[0])
                break
            if right == '|':
                not_search_flag = 0

    def First_Gene(self):
        while True:
            old_first = deepcopy(self.first)
            for not_end in self.leftpart:
                for right in self.GRAMMA[not_end]:
                    if right != 'e' and right[0] in self.VOL['T']:
                        if right[0] not in self.first[not_end]:
                            self.first[not_end].append(right[0])
                    elif right[0] in self.VOL['N']:
                        self.real_not_end = not_end
                        self.Find_First(right[0])
                        break
                if 'e' in self.GRAMMA[not_end]:
                    if 'e' not in self.first[not_end]:
                        self.first[not_end].append('e')
            if old_first == self.first:
                break

    def Follow_Give(self, dir, sour, type):
        if type == 0:
            for element in self.follow[sour]:
                if element not in self.follow[dir]:
                    self.follow[dir].append(element)
        if type == 1:
            for element in self.first[sour]:
                if element not in self.follow[dir]:
                    if element == 'e':
                        continue
                    else:
                        self.follow[dir].append(element)

    def Follow_Gene(self):
        self.follow['E'].append('#')
        while True:
            old_follow = deepcopy(self.follow)
            for test_not_end in self.leftpart:
                for not_end in self.leftpart:
                    for right in self.GRAMMA[not_end]:
                        if test_not_end in right:
                            if test_not_end == right[-1]:
                                #self.follow[test_not_end].append(self.follow[not_end])
                                self.Follow_Give(test_not_end, not_end, 0)
                                break
                            not_end_next = right[right.index(test_not_end) + 1]
                            if not_end_next in self.VOL['T']:
                                if not_end_next not in self.follow[test_not_end]:
                                    self.follow[test_not_end].append(not_end_next)
                            elif not_end_next in self.VOL['N']:
                                if 'e' not in self.first[not_end_next]:
                                    self.Follow_Give(test_not_end, not_end_next, 1)
                                    #self.follow[test_not_end].append(self.first[not_end_next])
                                else:
                                    self.Follow_Give(test_not_end, not_end_next, 1)
                                    self.Follow_Give(test_not_end, not_end, 0)
            if old_follow == self.follow:
                break

if __name__ == '__main__':
    test = Generator(GRAMMA, VOL)
    test.First_Gene()

    print("FIRST")
    for keys in test.leftpart:
        print(str(keys) + "::" + str(test.first[keys]))

    print("FOLLOW")
    test.Follow_Gene()
    for keys in test.leftpart:
        print(str(keys) + "::" + str(test.follow[keys]))