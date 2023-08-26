# -*- coding: utf-8 -*-

def sortlistpalithai(word): # เอเกกวณฺโณ อกฺขโร
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
        't': '.',
        'u': '–',
        'v': ',',
        'w': ';',
        'x': '[',
        'y': ']',
        'z': '(',
        'z1': ')',
        'z2': '’',
        'z3': '‘',
        'z4': '?',
        'z5': '…',
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

    # Alphabetic = Vowels + Consonants

    keysA = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f']
    havA = {x: Alphabetic[x] for x in keysA}

    Vowels = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    changA = {x: Alphabetic[x] for x in Vowels}

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

    data = convertcommand(word)  # นำ keys ที่ระบุไว้ในตอนที่ทำ dictionary อักษรโดยทำการเปลี่ยนตัวอักษรเป็น keys
    d = ''

    def sortconvert(data):
        for y in range(1, len(data)):
            for z in range(0, len(data) - 1):
                if y != z:
                    if data[y] > data[z]:
                        d = data[y]
                        data[y] = data[z]
                        data[z] = d
                        if True:
                            stud = True

        return data

    y = sortconvert(data)  # ทำการเรียงอักษรเบื้องต้น

    def sortreversed(y):
        i = []
        for a in range(0, len(y)):
            i.append(y[-1 - a])
        return i

    z = sortreversed(y)  # จำเป็นต้องใช้คำสั่งนี้เพียงเพราะว่า การสลับโดยไม่ทำการเรียงจำทำให้เกิดข้อผิดพลาดมากกว่า

    def swappedinput(z):  # this function is ทำงานโดยมีข้อผิดพลาดตรงที่เฉพาะเจาะจงต่อปริมาณของอักษร
        def swapped(z, a):
            for i in range(0, len(z)):
                if len(z[i]) == a:
                    j = 0
                    while j >= 0 and j < len(z[i]):
                        d = z[i]
                        k = j + 1
                        if d[j] == 'n' and d[k] in keysA:
                            s = d[j]
                            d[j] = d[k]
                            d[k] = s
                            j += 1
                        if d[j] == 'm' and d[k] in keysA:
                            s = d[j]
                            d[j] = d[k]
                            d[k] = s
                            j += 1
                        j += 1
                elif a == 1:
                    break

            return z

        swapped(z, 2)
        swapped(z, 3)
        swapped(z, 4)
        swapped(z, 5)
        swapped(z, 6)
        swapped(z, 7)
        swapped(z, 8)
        swapped(z, 9)
        swapped(z, 10)
        swapped(z, 11)
        swapped(z, 12)
        swapped(z, 13)
        swapped(z, 14)
        swapped(z, 15)
        swapped(z, 16)
        swapped(z, 17)
        swapped(z, 18)
        swapped(z, 19)
        swapped(z, 20)
        swapped(z, 21)
        swapped(z, 22)
        swapped(z, 23)
        swapped(z, 24)
        swapped(z, 25)
        swapped(z, 26)
        swapped(z, 27)
        swapped(z, 28)
        swapped(z, 29)
        swapped(z, 30)
        swapped(z, 31)
        swapped(z, 32)
        swapped(z, 33)
        swapped(z, 34)
        swapped(z, 35)
        swapped(z, 36)
        swapped(z, 37)
        swapped(z, 38)
        swapped(z, 39)
        swapped(z, 40)
        swapped(z, 41)
        swapped(z, 42)
        swapped(z, 43)
        swapped(z, 44)
        swapped(z, 45)
        swapped(z, 46)
        swapped(z, 47)
        swapped(z, 48)
        swapped(z, 49)
        swapped(z, 50)
        swapped(z, 51)
        swapped(z, 52)
        swapped(z, 53)
        swapped(z, 54)
        swapped(z, 55)
        swapped(z, 56)
        swapped(z, 57)
        swapped(z, 58)
        swapped(z, 59)
        swapped(z, 60)
        swapped(z, 61)
        swapped(z, 62)
        swapped(z, 63)
        swapped(z, 64)
        swapped(z, 65)
        swapped(z, 66)
        swapped(z, 67)
        swapped(z, 68)
        swapped(z, 69)
        swapped(z, 70)
        swapped(z, 71)
        swapped(z, 72)
        swapped(z, 73)
        swapped(z, 74)
        swapped(z, 75)
        swapped(z, 76)
        swapped(z, 77)
        swapped(z, 78)
        swapped(z, 79)
        swapped(z, 80)
        swapped(z, 81)
        swapped(z, 82)
        swapped(z, 83)
        swapped(z, 84)
        swapped(z, 85)
        swapped(z, 86)
        swapped(z, 87)
        swapped(z, 88)
        swapped(z, 89)
        swapped(z, 90)
        swapped(z, 91)
        swapped(z, 92)
        swapped(z, 93)
        swapped(z, 94)
        swapped(z, 95)
        swapped(z, 96)
        swapped(z, 97)
        swapped(z, 98)
        swapped(z, 99)
        swapped(z, 100)
        return z

    a = swappedinput(z)
    r = sortreversed(sortconvert(a))

    def swappedinputagain(r):  # this function is swapped กลับไปตำแหน่งก่อนหน้าเพราะว่าต้องการจะเปลี่ยนกลับไปเป็นภาษาไทย
        def swapped(r, a):
            for i in range(0, len(r)):
                if len(r[i]) == a:
                    j = len(r[i]) - 1
                    k = j - 1
                    while j >= 0 and j < len(r[i]):
                        d = r[i]
                        while k == j - 1 and k >= 0:
                            if d[k] in keysA and d[j] == 'n':
                                s = d[j]
                                d[j] = d[k]
                                d[k] = s
                                k -= 1
                            if d[k] in keysA and d[j] == 'm':
                                s = d[j]
                                d[j] = d[k]
                                d[k] = s
                                k -= 1
                            k -= 1

                        j -= 1
                elif a == 1:
                    break

            return r

        swapped(r, 2)
        swapped(r, 3)
        swapped(r, 4)
        swapped(r, 5)
        swapped(r, 6)
        swapped(r, 7)
        swapped(r, 8)
        swapped(r, 9)
        swapped(r, 10)
        swapped(r, 11)
        swapped(r, 12)
        swapped(r, 13)
        swapped(r, 14)
        swapped(r, 15)
        swapped(r, 16)
        swapped(r, 17)
        swapped(r, 18)
        swapped(r, 19)
        swapped(r, 20)
        swapped(r, 21)
        swapped(r, 22)
        swapped(r, 23)
        swapped(r, 24)
        swapped(r, 25)
        swapped(r, 26)
        swapped(r, 27)
        swapped(r, 28)
        swapped(r, 29)
        swapped(r, 30)
        swapped(r, 31)
        swapped(r, 32)
        swapped(r, 33)
        swapped(r, 34)
        swapped(r, 35)
        swapped(r, 36)
        swapped(r, 37)
        swapped(r, 38)
        swapped(r, 39)
        swapped(r, 40)
        swapped(r, 41)
        swapped(r, 42)
        swapped(r, 43)
        swapped(r, 44)
        swapped(r, 45)
        swapped(r, 46)
        swapped(r, 47)
        swapped(r, 48)
        swapped(r, 49)
        swapped(r, 50)
        swapped(r, 51)
        swapped(r, 52)
        swapped(r, 53)
        swapped(r, 54)
        swapped(r, 55)
        swapped(r, 56)
        swapped(r, 57)
        swapped(r, 58)
        swapped(r, 59)
        swapped(r, 60)
        swapped(r, 61)
        swapped(r, 62)
        swapped(r, 63)
        swapped(r, 64)
        swapped(r, 65)
        swapped(r, 66)
        swapped(r, 67)
        swapped(r, 68)
        swapped(r, 69)
        swapped(r, 70)
        swapped(r, 71)
        swapped(r, 72)
        swapped(r, 73)
        swapped(r, 74)
        swapped(r, 75)
        swapped(r, 76)
        swapped(r, 77)
        swapped(r, 78)
        swapped(r, 79)
        swapped(r, 80)
        swapped(r, 81)
        swapped(r, 82)
        swapped(r, 83)
        swapped(r, 84)
        swapped(r, 85)
        swapped(r, 86)
        swapped(r, 87)
        swapped(r, 88)
        swapped(r, 89)
        swapped(r, 90)
        swapped(r, 91)
        swapped(r, 92)
        swapped(r, 93)
        swapped(r, 94)
        swapped(r, 95)
        swapped(r, 96)
        swapped(r, 97)
        swapped(r, 98)
        swapped(r, 99)
        swapped(r, 100)
        return r

    bb = swappedinputagain(r)

    h = []
    g = []

    def converttovalues(bb):
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

    w = converttovalues(bb)

    goal = []

    def lstostring(w):
        out_str = ""
        for x in w:
            goal.append(out_str.join(x))
        return goal

    result = lstostring(w)
    return result



def vanna(kama):
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
             'U',
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
            if q[r] in keysA and q[r - 1] in keysD and q[r - 2] in keysA and q[r - 3] in keysC:
                w.append(q[r - 3] + q[r])
                w.append(q[r - 2] + q[r - 1])
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
                c.append(
                    b[t - 36] + b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[
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
                c.append(
                    b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
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
                c.append(
                    b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[
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
                c.append(
                    b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[
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
                c.append(
                    b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[
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
                c.append(
                    b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[
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
                c.append(
                    b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[
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
                c.append(
                    b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[
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
                c.append(
                    b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[
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
                c.append(
                    b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
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
                c.append(
                    b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[
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
                c.append(
                    b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[
                        t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                        t - 9] +
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
                c.append(
                    b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[
                        t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                        t - 8] +
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
                c.append(
                    b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[
                        t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[
                        t - 7] +
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
                c.append(
                    b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[
                        t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[
                        t - 6] + b[
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
                c.append(
                    b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[
                        t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                        t - 5] + b[
                        t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 21
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword:
                c.append(
                    b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[
                        t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                        t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 20
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword:
                c.append(
                    b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[
                        t - 2] + b[t - 1] + b[t])
                t -= 19
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword:
                c.append(
                    b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[
                        t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                        t - 2] + b[
                        t - 1] + b[t])
                t -= 18
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword:
                c.append(
                    b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                        t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                    b[t])
                t -= 17
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword:
                c.append(
                    b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                        t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 16
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword:
                c.append(
                    b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[
                        t - 7] +
                    b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 15
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword:
                c.append(
                    b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[
                        t - 6] +
                    b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 14
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword:
                c.append(
                    b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                        t - 5] +
                    b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 13
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword:
                c.append(
                    b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                        t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 12
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword and b[t - 11] in allword:
                c.append(
                    b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] +
                    b[
                        t - 2] +
                    b[t - 1] + b[t])
                t -= 11
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword:
                c.append(
                    b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] +
                    b[
                        t - 1] +
                    b[t])
                t -= 10
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword:
                c.append(
                    b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                    b[t])
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

    in_word = []

    def tostring_inlist(in_word):
        x = len(in_word)
        word = []
        for item in range(x):
            output = ""
            for w in in_word[item]:
                output += w
            word.append(output)
        return word

    space = " "
    convert = convertcommand(kama+space)
    group = groupword(lstostring(convert))
    form_word = converttovalues(group)

    return tostring_inlist(form_word)

# ปุพฺพมโธฐิตมสฺสรํ สเรน วิโยชเย
def pubbamadhodhita(word):
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
            if q[r] in keysA and q[r - 1] in keysD and q[r - 2] in keysA and q[r - 3] in keysC:
                w.append(q[r - 3] + q[r])
                w.append(q[r - 2] + q[r - 1])
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
                c.append(
                    b[t - 36] + b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[
                        t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[
                        t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[
                        t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
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
                c.append(
                    b[t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
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
                c.append(
                    b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[
                        t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[
                        t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[
                        t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                        t - 2] + b[t - 1] + b[t])
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
                c.append(
                    b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[
                        t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[
                        t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                        t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
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
                c.append(
                    b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[
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
                c.append(
                    b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[
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
                c.append(
                    b[t - 30] + b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[
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
                c.append(
                    b[t - 29] + b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[
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
                c.append(
                    b[t - 28] + b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[
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
                c.append(
                    b[t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
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
                c.append(
                    b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[
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
                c.append(
                    b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[
                        t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                        t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                    b[t])
                t -= 25
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword:
                c.append(
                    b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[
                        t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                        t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 24
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword:
                c.append(
                    b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[
                        t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[
                        t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 23
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword:
                c.append(
                    b[t - 22] + b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[
                        t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[
                        t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 22
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword:
                c.append(
                    b[t - 21] + b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[
                        t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                        t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 21
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword:
                c.append(
                    b[t - 20] + b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[
                        t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                        t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 20
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword:
                c.append(
                    b[t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 19
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword:
                c.append(
                    b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[
                        t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[
                        t - 2] + b[t - 1] + b[t])
                t -= 18
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword:
                c.append(
                    b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[
                        t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                    b[t])
                t -= 17
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword:
                c.append(
                    b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[
                        t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 16
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword:
                c.append(
                    b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[
                        t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 15
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword:
                c.append(b[t - 14] + b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[
                    t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 14
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword:
                c.append(b[t - 13] + b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[
                    t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 13
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword:
                c.append(b[t - 12] + b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[
                    t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 12
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword and b[t - 11] in allword:
                c.append(
                    b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] +
                    b[t - 2] +
                    b[t - 1] + b[t])
                t -= 11
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword:
                c.append(
                    b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] +
                    b[t - 1] +
                    b[t])
                t -= 10
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                t - 8] in allword and b[t - 9] in allword:
                c.append(
                    b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                    b[t])
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
        if z >= 1:
            x = z - 1
            for y in word:
                if z >= 0:
                    if y in vowel_sound:
                        iso.append(vowel_sound)
                        z = z - 2
                    elif y in consonant_palithai:
                        iso.append(vowel_sound)
                        iso.append(y + press_vowel)
                        z = z - 2
                    elif z == 1:
                        if y[z] not in consonant_para and y[z] not in vowel_textpubba and y[z] not in vowel_textpara and \
                                y[z - 1] in consonant_palithai:
                            iso.append(vowel_sound)
                            iso.append(y[z] + press_vowel)
                        elif y[z - 1] == "อ" and y[z] == "ํ":
                            iso.append(y[z - 1] + y[z])
                            z = z - 1
                        elif y[z - 1] in consonant_palithai and y[z] in consonant_para:
                            iso.append(vowel_sound + consonant_para)
                            iso.append(y[z - 1] + press_vowel)
                            z = z - 1
                        elif y[z - 1] in consonant_palithai and y[z] in vowel_textpubba:
                            iso.append(vowel_sound + y[z])
                            iso.append(y[z - 1] + press_vowel)
                            z = z - 1
                        elif y[z - 1] in consonant_palithai and y[z] in press_vowel:
                            iso.append(y[z - 1] + y[z])
                            z = z - 1
                        elif y[z - 1] in vowel_textpara and y[z] in consonant_palithai:
                            iso.append(y[z - 1] + vowel_sound)
                            iso.append(y[z] + press_vowel)
                            z = z - 1
                        elif y[z - 1] in vowel_textpara and y[z] == "อ":
                            iso.append(y[z - 1] + y[z])
                            z = z - 1
                        elif y[z - 1] == 'อ' and y[z] in vowel_textpubba:
                            iso.append(y[z - 1] + y[z])
                            z = z - 1
                        elif y[z - 1] == 'อ' and y[z] in consonant_palithai:
                            iso.append(vowel_sound)
                            iso.append(y[z] + press_vowel)
                            iso.append(vowel_sound)
                            z = z - 1

                        z = z - 1

                while z >= 0:
                    if y[z] == "ํ" and y[z - 1] in consonant_palithai:
                        iso.append(vowel_sound + consonant_para)
                        iso.append(y[z - 1] + press_vowel)
                        z = z - 2
                    elif y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] == "อ":
                        iso.append(y[z - 2] + y[z - 1] + y[z])
                        z = z - 3
                    elif y[z] == "ํ" and y[z - 1] == "ุ" and y[z - 2] in consonant_palithai:
                        iso.append(vowel_sound + y[z - 1] + y[z])
                        iso.append(y[z - 2] + press_vowel)
                        z = z - 3
                    elif y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] == "อ":
                        iso.append(y[z - 2] + y[z - 1] + y[z])
                        z = z - 3
                    elif y[z] == "ํ" and y[z - 1] == "ิ" and y[z - 2] in consonant_palithai:
                        iso.append(vowel_sound + y[z - 1] + y[z])
                        iso.append(y[z - 2] + press_vowel)
                        z = z - 3
                    elif y[z] == "ํ" and y[z - 1] == "อ":
                        iso.append(y[z - 1] + y[z])
                        z = z - 2

                    elif y[z] in vowel_textpubba and y[z - 1] in consonant_palithai:
                        iso.append(vowel_sound + y[z])
                        iso.append(y[z - 1] + press_vowel)
                        z = z - 2
                    elif y[z] in press_vowel and y[z - 1] in consonant_palithai:
                        iso.append(y[z - 1] + y[z])
                        z = z - 2
                    elif y[z] == "อ" and z == 0:
                        iso.append(y[z])
                        z = z - 1
                    elif y[z] == "อ" and y[z - 1] in vowel_textpara:
                        iso.append(y[z - 1] + y[z])
                        z = z - 2
                    elif y[z] in vowel_textpubba and y[z - 1] == 'อ':
                        iso.append(y[z - 1] + y[z])
                        z = z - 2
                    elif y[z] in consonant_palithai and y[z - 1] in vowel_textpara:
                        iso.append(y[z - 1] + vowel_sound)
                        iso.append(y[z] + press_vowel)
                        z = z - 2
                    elif y[z] in consonant_palithai:
                        iso.append(vowel_sound)
                        iso.append(y[z] + press_vowel)
                        z = z - 1
                    else:
                        iso.append(y[z])
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
        if space not in word and z == 2 and word[z - 1] == "ํ":
            convert = convertcommand(word + space)
            group = groupword(lstostring(convert))
            form_word = converttovalues(group)
            return isolate(lstostring(form_word), z - 1)
        elif space not in word and z >= 2:
            convert = convertcommand(word + space)
            group = groupword(lstostring(convert))
            form_word = converttovalues(group)
            return isolate(lstostring(form_word), z - 1)
        elif space not in word and z == 1:
            convert = convertcommand(word + space)
            group = groupword(lstostring(convert))
            form_word = converttovalues(group)
            return isolate(lstostring(form_word), z)
        elif space in word:
            pada = sentense_iso(word)
            samooha = []

            def cutsentense(j):
                z = len(pada[j])
                e = pada[j]
                if j >= 0 and j < len(pada) and len(pada[j]) == 2:
                    convert = convertcommand(pada[j] + space)
                    group = groupword(lstostring(convert))
                    form_word = converttovalues(group)
                    return isolate(lstostring(form_word), z - 1)
                elif j >= 0 and j < len(pada) and z > 2:
                    convert = convertcommand(pada[j] + space)
                    group = groupword(lstostring(convert))
                    form_word = converttovalues(group)
                    return isolate(lstostring(form_word), z - 1)
                elif j >= 0 and j < len(pada) and len(pada[j]) == 1:
                    convert = convertcommand(pada[j] + space)
                    group = groupword(lstostring(convert))
                    form_word = converttovalues(group)
                    return isolate(lstostring(form_word), z)

            l = len(pada)
            g = 0
            while g >= 0 and g < l:
                samooha.append(cutsentense(g))
                g += 1
            return samooha

    return separated_word(word)


# นเย ปรํ ยุตฺเต
def nayeparamyutte(word):
    from compose_yoga import sortreversed
    from compose_yoga import lstostring
    from compose_yoga import listtostring

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
    space = ' '


    s = pubbamadhodhita(word)
    z = len(s)
    wording = []
    z = z-1

    while z>0:
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
        elif s[z] in consonant_pubba and s[z-1] in space:
            a.append(' ')
            z = z-2
        elif s[z] in sadda or s[z] in sadda_textpara or s[z] in vowel_sound and s[z-1] in space:
            a.append(' ')
            z = z-2
        elif s[z] in space:
            a.append(' ')
            z = z-1
        else:
            a.append(s[z-1])
            z = z-1
        wording.append(a)

    return listtostring(sortreversed(lstostring(wording)))





def sortpada(list_word):  # อกฺขรสมูโห ปทํ
    def count_akkhara(word):
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

        keysA = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T','U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f']
        havA = {x: Alphabetic[x] for x in keysA}

        Vowels = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
        changA = {x: Alphabetic[x] for x in Vowels}

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


        roman_pali = {
                'a': 'อ',
                'ā': 'อา',
                'i': 'อิ',
                'ī': 'อี',
                'u': 'อุ',
                'ū': 'อู',
                'e': 'เอ',
                'o': 'โอ',
                'aṃ':'อํ',
                'iṃ':'อิํ',
                'uṃ':'อุํ',
                'k': 'กฺ',
                'kh': 'ขฺ',
                'g': 'คฺ',
                'gh': 'ฆฺ',
                'ṅ': 'งฺ',
                'c': 'จฺ',
                'ch': 'ฉฺ',
                'j': 'ชฺ',
                'jh': 'ฌฺ',
                'ñ': 'ญฺ',
                'ṭ': 'ฏฺ',
                'ṭh': 'ฐฺ',
                'ḍ': 'ฑฺ',
                'ḍh': 'ฒฺ',
                'ṇ': 'ณฺ',
                't': 'ตฺ',
                'th': 'ถฺ',
                'd': 'ทฺ',
                'dh': 'ธฺ',
                'n': 'นฺ',
                'p': 'ปฺ',
                'ph': 'ผฺ',
                'b': 'พฺ',
                'bh': 'ภฺ',
                'm': 'มฺ',
                'y': 'ยฺ',
                'r': 'รฺ',
                'l': 'ลฺ',
                'v': 'วฺ',
                's': 'สฺ',
                'h': 'หฺ',
                'ḷ': 'ฬฺ',
                'ṃ': 'ํ',
                ' ':' '
            }

        def changekeydict(roman):
            dict1 = dict()
            for key, value in roman.items():
                dict1[value] = key
            return dict1

        toroman = changekeydict(roman_pali)


        def listtostring(w):
            i = 0
            x = ""
            while i in range(len(w)):
                y = w[i]
                x = x+y
                i += 1
            return x

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




        def isolate(word):
            iso = []
            z = len(word)
            consonant_para = "ํ"
            vowel_sound = "อ"
            vowel_textpubba = ["า", "ิ", "ี", "ุ", "ู"]
            vowel_rassa = ["ิ", "ุ"]
            vowel_textpara = ["เ", "โ"]
            consonant_palithai = ["ก", "ข", "ค", "ฆ", "ง",
                                  "จ", "ฉ", "ช", "ฌ", "ญ",
                                  "ฏ", "ฐ", "ฑ", "ฒ", "ณ",
                                  "ต", "ถ", "ท", "ธ", "น",
                                  "ป", "ผ", "พ", "ภ", "ม",
                                  "ย", "ร", "ล", "ว", "ส",
                                  "ห", "ฬ", ""]
            press_vowel = "ฺ"
            space = " "
            x = 0
            y = word
            if x == z - 1:
                if y[z - 1] in consonant_palithai:
                    iso.append(vowel_sound)
                    iso.append(y[z - 1] + press_vowel)
                elif y[z - 1] in vowel_sound:
                    iso.append(vowel_sound)
            elif x in range(0, z):
                while x >= 0 and x < z:
                    if y[z - 2] in consonant_palithai and y[z - 1] in consonant_para:
                        iso.append(y[z - 1])
                        iso.append(vowel_sound)
                        iso.append(y[z - 2] + press_vowel)
                        z = z - 1
                    elif y[z - 2] in vowel_textpara and y[z - 1] in consonant_palithai:
                        iso.append(y[z - 2] + vowel_sound)
                        iso.append(y[z - 1] + press_vowel)
                        z = z - 1
                    elif y[z - 3] in consonant_palithai and y[z - 2] in vowel_textpubba and y[z - 1] in consonant_para:
                        iso.append(y[z - 1])
                        iso.append(vowel_sound + y[z - 2])
                        iso.append(y[z - 3] + press_vowel)
                        z = z - 2
                    elif y[z - 2] in consonant_palithai and y[z - 1] in press_vowel:
                        iso.append(y[z - 2] + y[z - 1])
                        z = z - 1
                    elif y[z - 2] in consonant_palithai and y[z - 1] in vowel_textpubba:
                        iso.append(vowel_sound + y[z - 1])
                        iso.append(y[z - 2] + press_vowel)
                        z = z - 1
                    elif y[z - 1] in consonant_palithai:
                        iso.append(vowel_sound)
                        iso.append(y[z - 1] + press_vowel)
                    if y[z - 1] in space:
                        iso.append(space)
                    if y[z - 2] in vowel_textpara and y[z - 1] in vowel_sound:
                        iso.append(y[z - 2] + vowel_sound)
                        z = z - 1
                    elif y[z - 1] in vowel_sound:
                        iso.append(y[z - 1])
                    elif y[z - 2] in vowel_sound and y[z - 1] in vowel_textpubba:
                        iso.append(y[z - 2] + y[z - 1])
                        z = z - 1
                    elif y[z - 2] in vowel_sound and y[z - 1] in consonant_para:
                        iso.append(y[z - 2] + y[z - 1])
                        z = z - 1
                    elif y[z - 3] in vowel_sound and y[z - 2] in vowel_textpubba and y[z - 1] in consonant_para:
                        iso.append(y[z - 3] + y[z - 2])
                        iso.append(y[z - 1])
                        z = z - 2

                    z = z - 1

            return iso

        xor = convertcommand(word)
        nor = converttovalues(lstostring(xor))
        kor = lstostring(nor)
        sadda = sortreversed(isolate(kor))

        sound = []
        for item in sadda:
            sound.append(toroman[item])

        sara = ['a','ā','i','ī','u','ū','e','o']
        count = 0
        for i in sound:
            while i in sara:
                i = 1
                count = count + i
        return count



    from source_pali import sortlistpalithai
    x = 0
    kam = []
    while x>=0 and x < len(list_word):
        y = count_akkhara(list_word[x])
        if y == 2:
            kam.append(list_word[x])
        x = x+1

    word = sortlistpalithai(kam)
    return word
