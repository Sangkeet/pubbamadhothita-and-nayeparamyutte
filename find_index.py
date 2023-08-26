# -*- coding:utf-8 -*-

from tipitaka_org import tipitaka



book = tipitaka



Alphabetic = {
    '0': 'อ',
    'h': 'า',
    'i': 'ิ',
    'j': 'ี',
    'k': 'ุ',
    'l': 'ู',
    'm': 'เ',
    'n': 'โ',
    'g': 'ํ',
    'o': 'ฺ',
    'p': ' ',
    'q': 'ฯ',
    'r': '\n',
    '1': '๑',
    '2': '๒',
    '3': '๓',
    '4': '๔',
    '5': '๕',
    '6': '๖',
    '7': '๗',
    '8': '๘',
    '9': '๙',
    's': '๐',
    's1': '§',
    's2': '+',
    's3': '`',
    's4': 'ै',
    's5': 'ऋ',
    't': '.',
    'u': '–',
    'u1': '-',
    'u2': '!',
    'v': ',',
    'w': ';',
    'x': '[',
    'y': ']',
    'y1': '=',
    'z': '(',
    'z1': ')',
    'z2': '’',
    'z3': '‘',
    'z4': '?',
    'z5': '…',
    'z6': 'ः',
    'A': 'ก',
    'B': 'ข',
    'C': 'ค',
    'D': 'ฆ',
    'E': 'ง',
    'F': 'จ',
    'G': 'ฉ',
    'H': 'ช',
    'I': 'ฌ',
    'J': 'ญ',
    'K': 'ฏ',
    'L': 'ฐ',
    'M': 'ฑ',
    'N': 'ฒ',
    'O': 'ณ',
    'P': 'ต',
    'Q': 'ถ',
    'R': 'ท',
    'S': 'ธ',
    'T': 'น',
    'U': 'ป',
    'V': 'ผ',
    'W': 'พ',
    'X': 'ภ',
    'Y': 'ม',
    'Z': 'ย',
    'a': 'ร',
    'b': 'ล',
    'c': 'ว',
    'd': 'ส',
    'e': 'ห',
    'f': 'ฬ'
}

keysA = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f']
havA = {x: Alphabetic[x] for x in keysA}

Vowels = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
changA = {x: Alphabetic[x] for x in Vowels}

keysB = ['h', 'i', 'j', 'k', 'l']
backA = {x: changA[x] for x in keysB}

def mergedict(dict1, dict2):
    dict3 = dict()
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            dict3[key1 + key2] = value1 + value2
    return dict3

keysC = ['m', 'n']
frontA = {x: changA[x] for x in keysC}

keysD = ['o']
haftA = {x: changA[x] for x in keysD}

keysE = ['g']
am = {x: changA[x] for x in keysE}

keysF = ['i']
im = {x: changA[x] for x in keysF}

def mergedict2(dict1, dict2, dict3):
    dict4 = dict()
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            for key3, value3 in dict3.items():
                dict4[key1 + key2 + key3] = value1 + value2 + value3
    return dict4

keysG = ['k']
um = {x: changA[x] for x in keysG}

group1 = havA
group2 = mergedict(havA, backA)
group3 = mergedict(frontA, havA)
group4 = mergedict(havA, haftA)
group5 = mergedict(havA, am)
group6 = mergedict2(havA, im, am)
group7 = mergedict2(havA, um, am)

wordpali = dict()
wordpali.update(group1)
wordpali.update(group2)
wordpali.update(group3)
wordpali.update(group4)
wordpali.update(group5)
wordpali.update(group6)
wordpali.update(group7)

allword = wordpali.keys()

cut_unit = ['p', 'q', 'r', '1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'z1', 'z2', 'z3', 'z4', 'z5']


def lstostring(w):
    g = []
    out_str= ""
    for x in w:
        g.append(out_str.join(x))
    return g


def sortreversed(y):
    i = []
    for a in range(0, len(y)):
        i.append(y[-1 - a])
    return i


def converttovalues(bb):
    g =[]
    for i in range(0, len(bb)):
        d = bb[i]

        def tovalues(d):
            h = []
            d = bb[i]
            j = 0
            while j >= 0 and j < len(d):
                w = Alphabetic[d[j]]
                h.append(w)
                j += 1
            return h

        g.append(tovalues(d))
    return g


def groupakkhara(q):
    r = len(q) - 1
    w = []
    while r >= 0 and r < len(q):
        if q[r] in keysA and q[r - 1] in keysC:
            w.append(q[r - 1] + q[r])
            r -= 2
        elif q[r] in keysE and q[r - 1] in ['i', 'k']:
            w.append(q[r - 2] + q[r - 1] + q[r])
            r -= 3
        elif q[r] in keysE and q[r - 1] in keysA:
            w.append(q[r - 1] + q[r])
            r -= 2
        elif q[r] in keysD and q[r - 1] in keysA:
            w.append(q[r - 1] + q[r])
            r -= 2
        elif q[r] in keysB and q[r - 1] in keysA:
            w.append(q[r - 1] + q[r])
            r -= 2
        else:
            w.append(q[r])
            r -= 1

    return sortreversed(w)

def convertfunction(x):
    u = []
    for y in x:
        j = list(Alphabetic.keys())[list(Alphabetic.values()).index(y)]
        u.append(j)
    return u


def convertcommand(x):
    j = []
    for i in range(0, len(x)):
        a = convertfunction(x[i])
        j.append(a)

    return j


def listtostring(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def total_index(some_ref):
    x = []
    findx = some_ref[0:-1]
    for item in findx:
        x.append(item)
    return len(x)






def find_index(word):
    totalword = total_index(book)
    i = 0
    j = []
    a = 0
    if len(word) == 1:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j


    if len(word) == 2:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j

    if len(word) == 3:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1] and book[i+2] == form_word[a+2]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j

    if len(word) == 4:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1] and book[i+2] == form_word[a+2] and book[i+3] == form_word[a+3]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j

    if len(word) == 5:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1] and book[i+2] == form_word[a+2] and book[i+3] == form_word[a+3] \
                    and book[i+4] == form_word[a+4]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j

    if len(word) == 6:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1] and book[i+2] == form_word[a+2] and book[i+3] == form_word[a+3] \
                    and book[i+4] == form_word[a+4] and book[i+5] == form_word[a+5]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j

    if len(word) == 7:
        while i >= 0 and i < totalword:
            if book[i] == form_word[a] and book[i+1] == form_word[a+1] and book[i+2] == form_word[a+2] and book[i+3] == form_word[a+3] \
                    and book[i+4] == form_word[a+4] and book[i+5] == form_word[a+5] and book[i+6] == form_word[a+6]:
                for k in range(0,len(form_word)):
                    j.append(i+k)
            i = i+1
        return j




if __name__ == '__main__':
    word = 'ฬวีชนี'
    convert = convertcommand(word)
    form_word = lstostring(converttovalues(groupakkhara(convert)))
    print(find_index(word))
