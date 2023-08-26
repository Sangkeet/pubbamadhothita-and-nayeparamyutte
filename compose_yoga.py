# -*- coding: utf-8 -*-

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

keysA = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f']
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
    out_str = ""
    for x in w:
        g.append(out_str.join(x))
    return g


def sortreversed(y):
    i = []
    for a in range(0, len(y)):
        i.append(y[-1 - a])
    return i


def converttovalues(bb):
    g = []
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


r = 0
w = []


def groupword(q):
    r = len(q) - 1
    c = []

    while r >= 0 and r < len(q):
        if q[r] in keysA and q[r - 1] in keysD and q[r-2] in keysA and q[r-3] in keysC:
            w.append(q[r - 3] + q[r])
            w.append(q[r-2] + q[r-1])
            r -= 4
        elif q[r] in keysA and q[r - 1] in keysC:
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
    b = sortreversed(w)
    i = 0
    t = len(b) - 1
    while t >= 0 and t < len(b):
        if b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
            t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword and b[t - 11] in allword and b[
            t - 12] in allword and b[t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[
            t - 16] in allword and b[t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[
            t - 20] in allword and b[t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[
            t - 24] in allword and b[t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[
            t - 28] in allword and b[t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[
            t - 32] in allword and b[t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[
            t - 36] in allword:
            c.append(b[t - 36] + b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[
                t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[
                         t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] +
                     b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                         t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 36
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
            t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword:
            c.append(b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                         t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] +
                     b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                         t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 35
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
            t - 33] in allword and b[t - 34] in allword:
            c.append(b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[
                t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[
                         t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] +
                     b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] +
                     b[t - 1] + b[t])
            t -= 34
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
            t - 33] in allword:
            c.append(b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[
                t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[
                         t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] +
                     b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                     b[t])
            t -= 33
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword:
            c.append(b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[
                t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[
                         t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                         t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 32
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword:
            c.append(b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[
                t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[
                         t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[
                         t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 31
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword and b[t - 30] in allword:
            c.append(b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[
                t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[
                         t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[
                         t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 30
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
            t - 29] in allword:
            c.append(b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[
                t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[
                         t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                         t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 29
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword:
            c.append(b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[
                t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[
                         t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                         t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 28
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword:
            c.append(b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                         t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                         t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 27
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword and b[t - 26] in allword:
            c.append(b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[
                t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[
                         t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                         t - 2] + b[t - 1] + b[t])
            t -= 26
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
            t - 25] in allword:
            c.append(b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[
                t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] +
                     b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 25
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword:
            c.append(b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[
                t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] +
                     b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 24
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword:
            c.append(b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[
                t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] +
                     b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 23
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword and b[t - 22] in allword:
            c.append(b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[
                t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                         t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 22
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
            t - 21] in allword:
            c.append(b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[
                t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                         t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 21
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword:
            c.append(b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[
                t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                         t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 20
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword:
            c.append(b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                         t - 2] + b[t - 1] + b[t])
            t -= 19
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword and b[t - 18] in allword:
            c.append(b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[
                t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[
                         t - 1] + b[t])
            t -= 18
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
            t - 17] in allword:
            c.append(b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 17
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword:
            c.append(b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 16
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword:
            c.append(
                b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] +
                b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 15
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword and b[t - 14] in allword:
            c.append(
                b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] +
                b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 14
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
            t - 13] in allword:
            c.append(
                b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] +
                b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 13
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and \
                b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
            t - 9] in \
                allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword:
            c.append(
                b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                    t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 12
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
            t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword and b[t - 11] in allword:
            c.append(
                b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                    t - 2] +
                b[t - 1] + b[t])
            t -= 11
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
            t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword:
            c.append(
                b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[
                    t - 1] +
                b[t])
            t -= 10
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
            t - 8] in allword and b[t - 9] in allword:
            c.append(
                b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 9
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
            t - 8] in allword:
            c.append(b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 8
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword:
            c.append(b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 7
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword:
            c.append(b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 6
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword and b[t - 5] in allword:
            c.append(b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 5
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
            t - 4] in allword:
            c.append(b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 4
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword:
            c.append(b[t - 3] + b[t - 2] + b[t - 1] + b[t])
            t -= 3
        elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword:
            c.append(b[t - 2] + b[t - 1] + b[t])
            t -= 2
        elif b[t] in allword and b[t - 1] in allword:
            c.append(b[t - 1] + b[t])
            t -= 1
        elif b[t] in allword:
            c.append(b[t])
        t -= 1

    return sortreversed(c)




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


def isolate(word, z):
    iso = []

    consonant_para = "ํ"
    vowel_sound = "อ"
    vowel_textpubba = ["า", "ิ", "ี", "ุ", "ู"]
    vowel_textpara = ["เ", "โ"]
    consonant_palithai = ["ก", "ข", "ค", "ฆ", "ง",
                          "จ", "ฉ", "ช", "ฌ", "ญ",
                          "ฏ", "ฐ", "ฑ", "ฒ", "ณ",
                          "ต", "ถ", "ท", "ธ", "น",
                          "ป", "ผ", "พ", "ภ", "ม",
                          "ย", "ร", "ล", "ว", "ส",
                          "ห", "ฬ", ""]
    press_vowel = "ฺ"
    x = 0
    y = word
    if z >= 1:
        x = z-1
        for y in word:
            if z >= 0:
                if y in consonant_palithai:
                    iso.append(vowel_sound)
                    iso.append(y + press_vowel)
                    z = z-2
                elif z == 1:
                    if y[z] not in vowel_textpubba and y[z] not in vowel_textpara and y[z-1] in consonant_palithai:
                        iso.append(vowel_sound)
                        iso.append(y[z] + press_vowel)
                    elif y[z-1] == "อ" and y[z] == "ํ":
                        iso.append(y[z - 1] + y[z])
                        z = z - 1
                    elif y[z-1] in consonant_palithai and y[z] == "ํ":
                        iso.append(vowel_sound + consonant_para)
                        iso.append(y[z - 1] + press_vowel)
                        z = z - 1
                    elif y[z-1] in consonant_palithai and y[z] in vowel_textpubba:
                        iso.append(vowel_sound + y[z])
                        iso.append(y[z - 1] + press_vowel)
                        z = z - 1
                    elif y[z-1] in consonant_palithai and y[z] in press_vowel:
                        iso.append(y[z - 1] + y[z])
                        z = z - 1
                    elif y[z-1] in vowel_textpara and y[z] in consonant_palithai:
                        iso.append(y[z - 1] + vowel_sound)
                        iso.append(y[z] + press_vowel)
                        z = z - 1
                    elif y[z-1] in vowel_textpara and y[z] == "อ":
                        iso.append(y[z - 1] + y[z])
                        z = z - 1
                    elif y[z-1] == 'อ' and y[z] in vowel_textpubba:
                        iso.append(y[z - 1] + y[z])
                        z = z - 1
                    elif y[z-1] == 'อ' and y[z] in consonant_palithai:
                        iso.append(vowel_sound)
                        iso.append(y[z]+press_vowel)
                        iso.append(vowel_sound)
                        z = z-1


                    z = z-1

            while z >= 0:
                if y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] == "อ":
                    iso.append(y[z - 2] + y[z - 1] + y[z])
                    z = z - 2
                elif y[z] == "ํ" and y[z - 1] == "ุ" and y[z - 2] in consonant_palithai :
                    iso.append(vowel_sound + y[z - 1] + y[z])
                    iso.append(y[z - 2] + press_vowel)
                    z = z - 2
                elif y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] == "อ":
                    iso.append(y[z - 2] + y[z - 1] + y[z])
                    z = z - 2
                elif y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] in consonant_palithai:
                    iso.append(vowel_sound + y[z - 1] + y[z])
                    iso.append(y[z - 2] + press_vowel)
                    z = z - 2
                elif y[z] == "ํ" and y[z-1] == "อ":
                    iso.append(y[z-1] + y[z])
                    z = z-1
                elif y[z] == "ํ" and y[z-1] in consonant_palithai:
                    iso.append(vowel_sound + consonant_para)
                    iso.append(y[z-1] + press_vowel)
                    z =z-1
                elif y[z] in vowel_textpubba and y[z-1] in consonant_palithai:
                    iso.append(vowel_sound + y[z])
                    iso.append(y[z-1] + press_vowel)
                    z = z-1
                elif y[z] in press_vowel and y[z-1] in consonant_palithai:
                    iso.append(y[z-1] + y[z])
                    z = z-1
                elif y[z] in consonant_palithai and y[z-1] in vowel_textpara:
                    iso.append(y[z-1] + vowel_sound)
                    iso.append(y[z] + press_vowel)
                    z = z-1
                elif y[z] == "อ" and y[z-1] in vowel_textpara:
                    iso.append(y[z-1] + y[z])
                    z = z - 1
                elif y[z] in vowel_textpubba and y[z - 1] == 'อ' :
                    iso.append(y[z - 1] + y[z])
                    z = z - 1
                elif y[z] in consonant_palithai:
                    iso.append(vowel_sound)
                    iso.append(y[z] + press_vowel)
                elif y[z] in vowel_sound:
                    iso.append(y[z])
                elif y[z] in consonant_palithai and y[z-1] == 'อ':
                    iso.append(y[z-1])


                z = z - 1


    return sortreversed(iso)


def sentense_iso(sentense):
    x = " "
    a = ""
    b = ""
    c = ""
    if x + x in sentense or x + x + x in sentense or x + x + x + x in sentense:
        a = x + x
        b = x + x + x
        c = x + x + x + x
        a = x
        b = a
        c = b
        z = sentense.split(c)

    z = sentense.split(x)

    return z


def separated_word(word):
    space = " "
    z = len(word)
    if space not in word and z >= 2:
        convert = convertcommand(word+space)
        group = groupword(lstostring(convert))
        form_word = converttovalues(group)
        return isolate(lstostring(form_word),z-1)
    elif space not in word and z == 1:
        convert = convertcommand(word+space)
        group = groupword(lstostring(convert))
        form_word = converttovalues(group)
        return isolate(lstostring(form_word),z)
    elif space in word:
        pada = sentense_iso(word)
        samooha = []

        def cutsentense(j):
            z = len(pada[j])
            if j >= 0 and j < len(pada) and len(pada[j]) > 2:
                convert = convertcommand(pada[j] + space)
                group = groupword(lstostring(convert))
                form_word = converttovalues(group)
                return isolate(lstostring(form_word), z-1)
            elif j >= 0 and j < len(pada) and  len(pada[j]) == 1:
                convert = convertcommand(pada[j] + space)
                group = groupword(lstostring(convert))
                form_word = converttovalues(group)
                return isolate(lstostring(form_word),z)
            elif j >= 0 and j < len(pada) and  len(pada[j]) == 2:
                convert = convertcommand(pada[j] + space)
                group = groupword(lstostring(convert))
                form_word = converttovalues(group)
                return isolate(lstostring(form_word), z-1)

        l = len(pada)
        g = 0
        while g >= 0 and g < l:
            samooha.append(cutsentense(g))
            g += 1
        return samooha




def compose_yoga(word):
    consonant_pubba = ["กฺ", "ขฺ", "คฺ", "ฆฺ", "งฺ",
                       "จฺ", "ฉฺ", "ชฺ", "ฌฺ", "ญฺ",
                       "ฏฺ", "ฐฺ", "ฑฺ", "ฒฺ", "ณฺ",
                       "ตฺ", "ถฺ", "ทฺ", "ธฺ", "นฺ",
                       "ปฺ", "ผฺ", "พฺ", "ภฺ", "มฺ",
                       "ยฺ", "รฺ", "ลฺ", "วฺ", "สฺ",
                       "หฺ", "ฬฺ"]
    sadda = ["อา","อิ","อี","อุ","อู","อํ","อิํ","อุํ"]
    vowel_sound = "อ"
    sadda_textpara = ["เอ","โอ"]
    kam = word

    word_comming = []
    group = groupword(lstostring(word))
    form_word = sortreversed(converttovalues(group))
    list_word = lstostring(form_word)
    if len(list_word) == 1:
        c = list_word[0]
        s = separated_word(c)
        z = len(s)
        wording = []
        z = z - 1
        while z > 0:
            y = 1
            a = []
            h = []
            alpha_3 = s[z]
            alpha_2 = s[z-1]
            alpha_1 = s[z-2]
            q = len(alpha_3)
            if (s[z] in sadda_textpara or s[z] in sadda or s[z] in vowel_sound) and s[z - 1] in consonant_pubba and (
                    s[z - 2] in sadda_textpara or s[z - 2] in sadda or s[z - 2] in vowel_sound) and z> 2:
                if s[z - 1] in consonant_pubba and s[z] in sadda or s[z] in vowel_sound:
                    if s[z] in sadda or s[z] in vowel_sound:
                        h.append(alpha_2[0])
                        if len(s[z]) == 2:
                            while y >= 0 and y < q:
                                h.append(alpha_3[y])
                                y = y + 1

                elif s[z] in sadda_textpara and s[z - 1] in consonant_pubba:
                    h.append(alpha_3[0])
                    h.append(alpha_2[0])

                a.append(listtostring(h))
                z = z - 1
            elif s[z] in consonant_pubba and (s[z - 1] in sadda or s[z - 1] in sadda_textpara or s[z - 1] in vowel_sound) and s[z - 2] in consonant_pubba:
                if s[z - 1] in sadda or s[z - 1] in vowel_sound or s[z-1] in sadda_textpara and s[z - 2] in consonant_pubba:
                    if s[z - 1] in sadda or s[z - 1] in vowel_sound and s[z - 2] in consonant_pubba:
                        h.append(alpha_1[0])
                        if len(s[z-1]) == 2:
                            while y >= 0 and y < q:
                                h.append(alpha_2[y])
                                y = y + 1
                    elif s[z - 1] in sadda_textpara and s[z - 2] in consonant_pubba:
                        h.append(alpha_2[0])
                        h.append(alpha_1[0])

                a.append(listtostring(h))
                z = z-2
            elif s[z] in sadda_textpara or s[z] in sadda or s[z] in vowel_sound and s[z - 1] in consonant_pubba and s[
                z - 2] in consonant_pubba:
                if (s[z] in sadda or s[z] in vowel_sound) and s[z - 1] in consonant_pubba:
                    if s[z] in sadda or s[z] in vowel_sound:
                        h.append(alpha_2[0])
                        if len(s[z]) >= 2:
                            while y >= 0 and y < q:
                                h.append(alpha_3[y])
                                y = y + 1

                if s[z] in sadda_textpara and s[z - 1] in consonant_pubba:
                    h.append(alpha_3[0])
                    h.append(alpha_2[0])

                a.append(listtostring(h))
                z = z-1
            elif s[z] in consonant_pubba and s[z - 1] in consonant_pubba and s[z - 2] in sadda or s[
                z - 2] in sadda_textpara or s[z - 2] in vowel_sound:
                a.append(s[z - 1])
                z = z-1
            elif s[z] in consonant_pubba and s[z - 1] in consonant_pubba:
                a.append(s[z - 1])
                z = z-1
            elif s[z] in vowel_sound and s[z-1] in consonant_pubba:
                a.append(alpha_2[0])
                z = z-2
            elif s[z] in sadda or s[z] in sadda_textpara or s[z] in vowel_sound:
                a.append(s[z])
                z = z-1
            else:
                a.append(s[z-1])
                z = z-1
            wording.append(a)

        return sortreversed(lstostring(wording))

    elif len(list_word) > 1:
        l = len(list_word)
        i = 0
        while i >= 0 and i < l:
            c = list_word[i]
            s = separated_word(c)
            z = len(s)
            wording = []
            z = z-1
            while z > 0:
                a = []
                y = 1
                h = []
                alpha_3 = s[z]
                alpha_2 = s[z-1]
                alpha_1 = s[z-2]
                q = len(alpha_3)


                if (s[z] in sadda_textpara or s[z] in sadda or s[z] in vowel_sound) and s[z-1] in consonant_pubba  and (s[z-2] in sadda_textpara or s[z-2] in sadda or s[z-2] in vowel_sound):
                    if s[z-1] in consonant_pubba and s[z] in sadda or s[z] in vowel_sound:
                        if s[z] in sadda or s[z] in vowel_sound:
                            h.append(alpha_2[0])
                            while y >= 0 and y < q:
                                h.append(alpha_3[y])
                                y = y+1
                    if s[z] in sadda_textpara and s[z-1] in consonant_pubba:
                        h.append(alpha_3[0])
                        h.append(alpha_2[0])

                    a.append(listtostring(h))
                    z = z-2
                elif s[z] in consonant_pubba and s[z-1] in sadda and s[z-2] in consonant_pubba:
                    h.append(alpha_1[0])
                    h.append(alpha_2[1])
                    a.append(listtostring(h))
                    z = z-2
                elif s[z] in consonant_pubba and s[z-1] in vowel_sound and s[z-2] in consonant_pubba:
                    h.append(alpha_1[0])
                    a.append(listtostring(h))
                    z = z-2
                elif s[z] in consonant_pubba and s[z-1] in sadda_textpara and s[z-2] in consonant_pubba:
                    h.append(alpha_2[0])
                    h.append(alpha_1[0])
                    a.append(listtostring(h))
                    z = z-2
                elif s[z] in consonant_pubba and (s[z-1] in sadda_textpara or s[z-1] in sadda or s[z-1] in vowel_sound) and (s[z-2] in sadda_textpara or s[z-2] in sadda or s[z-2] in vowel_sound):
                    a.append(s[z-1])
                    z = z-2
                elif (s[z] in sadda_textpara or s[z] in sadda or s[z] in vowel_sound) and s[z - 1] in consonant_pubba and s[z-2] in consonant_pubba:
                    if (s[z] in sadda or s[z] in vowel_sound) and s[z - 1] in consonant_pubba:
                        if s[z] in sadda or s[z] in vowel_sound:
                            h.append(alpha_2[0])
                            while y >= 0 and y < q:
                                h.append(alpha_3[y])
                                y = y + 1

                    if s[z] in sadda_textpara and s[z - 1] in consonant_pubba:
                        h.append(alpha_3[0])
                        h.append(alpha_2[0])

                    a.append(listtostring(h))
                    z = z-1
                elif s[z] in consonant_pubba and s[z-1] in consonant_pubba and s[z-2] in sadda or s[z-2] in sadda_textpara or s[z-2] in vowel_sound:
                    a.append(s[z-1])
                    z = z-1
                elif s[z] in consonant_pubba and s[z] in consonant_pubba and s[z] in consonant_pubba:
                    a.append(s[z-1])
                    z = z-1
                elif s[z] in consonant_pubba and s[z-1] in consonant_pubba:
                    a.append(s[z-1])
                    z = z-1
                elif s[z] in consonant_pubba and (s[z-1] in vowel_sound or s[z-1] in sadda or s[z-1] in sadda_textpara) and (s[z-2] in vowel_sound or s[z-2] in sadda or s[z-2] in sadda_textpara):
                    z = z-1
                elif s[z] in consonant_pubba and (s[z-1] in vowel_sound or s[z-1] in sadda or s[z-1] in sadda_textpara):
                    a.append(s[z-1])
                    z = z-1
                elif s[z] in vowel_sound and (s[z-1] in sadda or s[z-1] in sadda_textpara):
                    a.append(s[z])
                    z = z-1
                elif s[z] in sadda or s[z] in sadda_textpara:
                    a.append(s[z])
                    z = z-1
                else:
                    a.append(s[z])
                    z = z-1

                wording.append(a)
            if z == 0 and len(s) % 2 == 1 and s[z] not in consonant_pubba:
                wording.append(s[z])




            word_comming.append(sortreversed(lstostring(wording)))
            i = i+1
        return word_comming




if __name__ == '__main__':
    wordk = "อนุคฺคตานิ"
    vajana = separated_word(wordk)
    print(vajana)
    compose = compose_yoga(vajana)
    print(compose)

# ปุพฺพมโธฐิตมสฺสรํ สเรน วิโยชเย
# นเย ปรํ ยุตฺเต
