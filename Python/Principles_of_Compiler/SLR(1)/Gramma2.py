from collections import OrderedDict
'''
GRAMMA = OrderedDict()
GRAMMA['E'] = [['E', '+', 'T'], '|', ['E', '-', 'T'], '|', 'T']
GRAMMA['T'] = [['T', '*', 'F'], '|', ['T', '/', 'F'], '|', 'F']
GRAMMA['F'] = [['(', 'E', ')'], '|', 'i']
GRAMMA['V'] = ['i', '|']
'''
'''
GRAMMA = OrderedDict()
GRAMMA['E'] = [['b', 'D', ';', 'S', 'a'], '|']
GRAMMA['D'] = [['D', ';', 'd'], '|', 'd']
GRAMMA['S'] = [['s', ';', 'S'], '|', 's']
'''
GRAMMA = OrderedDict()
GRAMMA['E'] = ['A', 'B']
GRAMMA['A'] = [['a', 'A', 'b'], 'c']
GRAMMA['B'] = [['a', 'B', 'b'], 'd']
'''
VOL = {
    'N' : ['E', 'E_', 'T', 'T_', 'F', 'E', 'A', 'M', 'D', 'S', 'B'],
    'T' : ['+', '-', '*', '/', '(', ')', 'i', '#', ';', 's', 'd', 'a', 'b', 'c']
}
'''
VOL = {
    'N' : ['E', 'A', 'B'],
    'T' : ['a', 'b', 'c', 'd', '#']
}