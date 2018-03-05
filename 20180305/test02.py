list = ['bf', 'gxaam', 'fg', 'qnqbd', 'kcq', 'oer', 'bjh', 'xn', 'mt', 'mscf', 'bd', 'sibl', 'cdlx', 'pbjql', 'btth', 'qpdsg', 'jbx', 'ufk', 'klmjz', 'bp', 'ovrgo', 'uijfs', 'ii', 'fi', 'ayqb', 'rqsf', 'glae', 'phrz', 'zkm', 'nf', 'farej', 'mdcul', 'ijzct', 'sh', 'gz', 'dieze', 'wjuov', 'sosx', 'kgddm', 'tqhl', 'ownh', 'etqhn', 'uo', 'deps', 'japqi', 'fxb', 'ew', 'gv', 'cgnj', 'ab', 'jb', 'fj', 'oyp', 'ktmw', 'wx', 'fanrz', 'uldj', 'tbw', 'bv', 'mw', 'yxu', 'szv', 'hgidm', 'cfyq', 'mwe', 'gykr', 'lfej', 'genw', 'vi', 'mwb', 'ttuz', 'rn', 'pylo', 'hpigw', 'yqmq', 'isle', 'gkha', 'mw', 'ii', 'hltzh', 'hwy', 'giv', 'novj', 'ycam', 'zt', 'dvqgr', 'ch', 'acnz', 'zlcnh', 'jm', 'ksxo', 'inox', 'rr', 'ut', 'gd', 'nr', 'sxxif', 'zvlov', 'xj']

list.sort()

data_in = str(input())

def binary_search(list, target):
    length = len(list)
    begin = 0
    end = length - 1

    while(begin <= end):
            middle = (begin + end) // 2
            if(list[middle] == target):
                return middle
            elif(str(list[middle]) < str(target)):
                begin = middle + 1
            else:
                end = middle - 1

print(binary_search(list, data_in))

