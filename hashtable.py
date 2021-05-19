########################
# HASHTABLE
########################

class HashTable:
    def __init__(self, length=16):
        self.length = length
        self.table = [''] * length

    def __repr__(self):
        rep = ' | '.join(str(e) for e in self.table)
        return rep

    def __hashFunc(self, data):
        hashval = 0
        data = str(data)
        for letter in data:
            hashval += ord(letter)
        return hashval % self.length

    def insert(self, data):
        pos = self.__hashFunc(data)

        while pos < self.length:

            if self.table[pos] == data: return True

            if self.table[pos] == '':
                self.table[pos] = data
                break
            else:
                pos += 1
                if pos >= self.length: return False

        return True

    def removeData(self, data):
        if self.inTable(data) == True:
            pos = self.find(data)
            print(pos)
            if self.removePos(pos): return True
            else: return False
        else: return False

    def removePos(self, pos):
        if pos >= 0 and pos < self.length:
            self.table[pos] = ''
            return True
        else: return False

    def find(self, data, pos=-1):
        if pos == -1: pos = self.__hashFunc(data)
        
        if pos >= self.length: return False

        if self.table[pos] != data:
            self.find(data, pos+1)
        else: return False

    def inTable(self, data):
        if self.find(data) == False: return False
        else: return True
        
    def getTable(self):
        return self.table