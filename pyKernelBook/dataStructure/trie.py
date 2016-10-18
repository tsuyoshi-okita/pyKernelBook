# -*- coding: utf-8 -*-

from utfLib import smart_str

class Trie:
    """
    triple = [num, value, {prefix}]
      num : num of triples
      value: contents are existed if it is a leaf, None if it is a node
      prefix: triples will be placed here
     self._trie = [1, None, {prefix}]

    examples:
      triple = [1, None, {}]
      triple = [1, None, {[1, 'a': {}]}]
      triple = [1, None, {[1, 'a': {[1, 'b', {[1, 'c': {[1, None, {}]}]}]}]}]
    """

    def __init__(self, data=None, type=None):
        if (type is None):
            if data is None:
                self._trie = [0, None, {}]
            else:
                self._trie = data
        elif (type == 'seqAuto'):
            self._trie = [0, None, {}]
            self.seq2trieAuto(data)
        elif (type == 'seqPair'):
            self._trie = [0, None, {}]
            self.seq2trieValue(data)
        elif (type == 'trie'):
            self._trie = data
        else:
            raise TypeError, 'Type should be either {trie, seqAuto, seqPair}.'

    def __del__(self):
        del self._trie

    def __len__(self):
        return self._trie[0]

    def __eq__(self, trie):
        return self._trie == trie._trie

    def __setitem__(self, key, value):
        if not(self.__contains__(key)):
            curr_triple = self._trie
            for ch in key:
                curr_triple[0] += 1
                next_triple = curr_triple[2]
                curr_triple = next_triple.setdefault(ch, [0, None, {}])
            curr_triple[1] = value
            curr_triple[0] += 1
        else:
            raise TypeError, 'This key is already asigned.'

    def __delitem__(self, key):
        try:
            triple = self.__getitem__(key)
        except KeyError:
            return False
        curr_triple = self._trie
        curr_triple[0] -= 1
        for ch in key:
            curr_triple = curr_triple[2][ch]
            if (curr_triple[0]==1):
                del previous_triple[2][ch]
            curr_triple[0] -= 1
            previous_triple = curr_triple
            previous_ch = ch

    def __getitem__(self, key):
        curr_triple = self._trie
        for ch in key:
            curr_triple = curr_triple[2][ch]
        return curr_triple[1]

    def __contains__(self, key):
        curr_triple = self._trie
        for ch in key:
            next_triple = curr_triple[2]
            if ch in next_triple:
                curr_triple = next_triple[ch]
            else:
                return False
        return True

    def __str__(self, part=None):
        print '##'
        if (part is None):
            part = self._trie
        for i in part:
            if isinstance (i, list):
                for j in i:
                    j.__str__(j)
            elif isinstance (i, dict):
                for j in i.keys():
                    print i[j],
                    self.__str__(i[j])
                print
            elif (i is None):
                pass
            else:
                print '@',smart_str(i),'_@'
        return smart_str(self._trie)        

    def __repr__(self):
        return

    def leaves(self):
        curr_triple = self._trie
        keys = curr_triple[2].keys()
        prefix = keys
        tripleList = []
        for i in range(len(keys)):
            if (curr_triple[2][keys[i]][0]>curr_triple[2][keys[i]][2].keys()):
                tripleList.append(prefix[i])
            if (curr_triple[2][keys[i]][2] == {}):
                result = keys[i]
            else:
                result = self.getChildren(prefix[i], curr_triple[2][keys[i]])
            for j in result:
#                print prefix, j
                tripleList.append(j)
        return tripleList

    def getChildren(self, key, triple):
        tmpTrippleList = []
        curr_triple = triple
        tripleList = []
        keys = curr_triple[2].keys()
        for i in keys:
            if not(curr_triple[2][i][2]=={}):
                if not(curr_triple[2][i][0]==len(curr_triple[2][i][2])):
                    tmpTrippleList.append(key[0]+i)
                next_triple = curr_triple[2][i]
                tmpList = []
                tmpList.append(key[0]+i)
                child_triple = self.getChildren(tmpList, next_triple)
                for k in child_triple:
                    tmpTrippleList.append(k)
            else:
                tmpTrippleList.append(key[0]+i)
        return tmpTrippleList

    def findPrefix(self, key):
        curr_triple = self._trie
        remainder = key
        for ch in key:
            if ch in curr_triple[2]:
                curr_triple = curr_triple[2][ch]
            else:
                return curr_triple[1], remainder
            remainder = remainder[1:]
        return curr_triple[1], remainder

    def getRoot(self):
        curr_triple = self._trie
        return curr_triple[2].keys()

    def subtrie(self, key):
        curr_triple = self._trie
        for ch in key:
            try:            
                curr_triple = curr_triple[2][ch]
            except KeyError:
                return Trie(None)
        return Trie(curr_triple,'trie')

    def trie2seq(self, trie):
        return trie.leaves()

    def seq2trieAuto(self, data):
        for i,iData in enumerate(data):
            self.__setitem__(iData, i)
#        globalID = 1            
#        for i in data:
#            self.__setitem__(i, int(globalID))
#            globalID += 1
            
    def seq2trieValue(self, data):
        print len(data)
        for i in range(len(data)):
            self.__setitem__(data[i][0],data[i][1])

    def getSeq(self):
        return self.leaves()

    def getTrie(self):
        return self._trie

    def set(self, key, value):
        self.__setitem__(key, value)

    def remove(self, key):
        self.__delitem__(key)

def demo():
    seqAuto = ['サンプル','A','Bon','Bot','Bonabi','Bonetter','Alice in Wonder']
    seqPair = [['chat','cat'],['hunt','dog'],['or','water'],['elle','she'],['il','he'],['spectacle','spectacle']]

    t = Trie(seqAuto,'seqAuto')
    print t
    t.set('Helen',10)
    for i in t.leaves():
        print smart_str(t)
#    print 't=',t.leaves()
    m = t.subtrie('A')
    print 't=',t.getRoot()
    print 't=',m.getRoot()

    t2 = Trie(seqPair,'seqPair')
    print t2
    print 't2=',t2.leaves()

    t.remove('Bot')
    t.remove('Bon')
    print 't=',t.leaves()
#    print 't=',t.getTrie()
    print t.subtrie('Ali')
    print t.findPrefix('Ali')
    print t.findPrefix('Bon')
    print t.findPrefix('Bona')
    print t.findPrefix('Bonabi')
    print 't=',t.leaves()

if __name__ == '__main__':
    demo()


