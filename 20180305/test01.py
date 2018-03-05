list = ['am', 'as', 'avcg', 'avcpb', 'be', 'bfpp', 'buth', 'cd', 'cd', 'cf', 'cuvgr', 'cvbb', 'cvv', 'cxcxj', 'dolyd', 'ds', 'dv', 'eb', 'eqd', 'eqjqr', 'esq', 'fjtzd', 'fkof', 'gevl', 'gppn', 'gpt', 'gv', 'gvcfz', 'gxybz', 'hkxi', 'hsls', 'huxug', 'hwebg', 'hxftn', 'hz', 'iif', 'inbjl', 'jbabh', 'jf', 'ju', 'ju', 'kc', 'kglxq', 'kpgqb', 'kznt', 'lkz', 'ltxr', 'mazdr', 'mihgh', 'mpht', 'mrqmb', 'mtc', 'mx', 'nst', 'nvlan', 'nvq', 'odktu', 'oheuk', 'oivfw', 'okvlx', 'pauuj', 'pnsbv', 'qz', 'rdfb', 'rf', 'rfd', 'rluc', 'rrrp', 'sexh', 'szhha', 'tmdi', 'to', 'tpk', 'uekpd', 'uf', 'ulu', 'uqstm', 'ur', 'vekhe', 'vgr', 'vndqw', 'vnx', 'vq', 'vrzxn', 'vxr', 'wjcne', 'wkuip', 'wqxoq', 'xgl', 'xkvzc', 'xmrju', 'xt', 'xz', 'yq', 'ytsae', 'zak', 'zcut', 'zp', 'zwn', 'zybou']

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

