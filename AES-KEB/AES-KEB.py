from bitarray import bitarray

class BitArray(object) :
    def __init__(self, ba):
        self.bitarray = ba
    def toHex(self):
        mult = 1
        temp = 0
        result = ""
        for i in range (3,-1,-1):
            temp = temp + self.bitarray[i] * mult
            mult = mult * 2
        if (temp > 9):
            result = result + chr(ord('a') +(temp - 10))
        else :
            result = result + chr(ord('0') + (temp))
        mult = 1
        temp = 0
        for i in range (7,3,-1):
            temp = temp + self.bitarray[i] * mult
            mult = mult * 2
        if (temp > 9):
            result = result + chr(ord('a') +(temp - 10))
        else :
            result = result + chr(ord('0') + (temp))
        return result
    def xor(self, a):
        return BitArray(self.bitarray ^ a.bitarray)

class Word(object):
    """docstring for Word"""
    def __init__(self, arg):
        self.s = []
        self.s.append(arg[0])
        self.s.append(arg[1])
        self.s.append(arg[2])
        self.s.append(arg[3])
    def toHex(self):
        return self.s[0].toHex() + self.s[1].toHex() +
self.s[2].toHex()+ self.s[3].toHex()
    def getIndex(self, index):
        if (index < 4):
            return self.s[index]
    def shift(self):
        return Word([self.s[3], self.s[0], self.s[1], self.s[2]])

class Words(object):
    """docstring for Words"""
    def __init__(self, arg):
        self.w = []
        self.length = len(arg)
        for i in xrange(1,len(arg)):
            self.w.append(arg[i])
    def getIndex(self, index):
        if (index < self.length):
            return self.w[index]

class SBox(object):
    """docstring for SBox"""
    def __init__(self, arg):
        self.arg = arg

def Rot(w1):
    return w1.shift()