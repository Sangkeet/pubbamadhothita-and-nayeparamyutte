# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# Maximum file size (kilobytes) IDE should provide code assistance for.
# The larger file is the slower its editor works and higher overall system memory requirements are
# if code assistance is enabled. Remove this property or set to very large number if you need
# code assistance for any files available regardless their size.
#-----------------------------------------------------------------------


def sortlistpalithai(word):
    Alphabetic = {
             '0':'อ',
             'h':'า',
             'i':'ิ',
             'j':'ี',
             'k':'ุ',
             'l':'ู',
             'm':'เ',
             'n':'โ',
             'g':'ํ',
             'o':'ฺ',
            'p':' ',
            'q':'ฯ',
            'r':'\n',
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
        'A' : 'ก',
        'B' : 'ข',
        'C' : 'ค',
        'D' : 'ฆ',
        'E' : 'ง',
        'F' : 'จ',
        'G' : 'ฉ',
        'H' : 'ช',
        'I' : 'ฌ',
        'J' : 'ญ',
        'K' : 'ฏ',
        'L' : 'ฐ',
        'M' : 'ฑ',
        'N' : 'ฒ',
        'O' : 'ณ',
        'P' : 'ต',
        'Q' : 'ถ',
        'R' : 'ท',
        'S' : 'ธ',
        'T' : 'น',
        'U' : 'ป',
        'V' : 'ผ',
        'W' : 'พ',
        'X' : 'ภ',
        'Y' : 'ม',
        'Z' : 'ย',
        'a' : 'ร',
        'b' : 'ล',
        'c' : 'ว',
        'd' : 'ส',
        'e' : 'ห',
        'f' : 'ฬ'
    }


    #Alphabetic = Vowels + Consonants


    keysA = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f']
    havA = {x:Alphabetic[x] for x in keysA}

    Vowels = ['g','h','i','j','k','l','m','n','o']
    changA = {x:Alphabetic[x] for x in Vowels}


    def convertfunction(x):
        u = []
        for y in x:
            j = list(Alphabetic.keys())[list(Alphabetic.values()).index(y)]
            u.append(j)
        return u


    def convertcommand(x):
        j = []
        for i in range(0,len(x)):
            a = convertfunction(x[i])
            j.append(a)

        return j


    data = convertcommand(word)  #นำ keys ที่ระบุไว้ในตอนที่ทำ dictionary อักษรโดยทำการเปลี่ยนตัวอักษรเป็น keys
    d = ''
    def sortconvert(data):
        for y in range(1,len(data)):
            for z in range(0,len(data)-1):
                if y != z:
                    if data[y] > data[z]:
                        d = data[y]
                        data[y] = data[z]
                        data[z] = d
                        if True:
                            stud = True


        return data

    y = sortconvert(data)  #ทำการเรียงอักษรเบื้องต้น

    def sortreversed(y):
        i = []
        for a in range(0,len(y)):
            i.append(y[-1-a])
        return i


    z = sortreversed(y)  #จำเป็นต้องใช้คำสั่งนี้เพียงเพราะว่า การสลับโดยไม่ทำการเรียงจำทำให้เกิดข้อผิดพลาดมากกว่า

    def swappedinput(z): #this function is ทำงานโดยมีข้อผิดพลาดตรงที่เฉพาะเจาะจงต่อปริมาณของอักษร
        def swapped(z,a):
            for i in range(0,len(z)):
                if len(z[i]) == a:
                    j = 0
                    while j >= 0 and j < len(z[i]):
                        d = z[i]
                        k = j + 1
                        if d[j] == 'n' and d[k] in keysA:
                            s = d[j]
                            d[j] = d[k]
                            d[k] = s
                            j+=1
                        if d[j] == 'm' and d[k] in keysA:
                            s = d[j]
                            d[j] = d[k]
                            d[k] = s
                            j += 1
                        j +=1
                elif a == 1:
                    break

            return z

        swapped(z,2)
        swapped(z,3)
        swapped(z,4)
        swapped(z,5)
        swapped(z,6)
        swapped(z,7)
        swapped(z,8)
        swapped(z,9)
        swapped(z,10)
        swapped(z,11)
        swapped(z,12)
        swapped(z,13)
        swapped(z,14)
        swapped(z,15)
        swapped(z,16)
        swapped(z,17)
        swapped(z,18)
        swapped(z,19)
        swapped(z,20)
        swapped(z,21)
        swapped(z,22)
        swapped(z,23)
        swapped(z,24)
        swapped(z,25)
        swapped(z,26)
        swapped(z,27)
        swapped(z,28)
        swapped(z,29)
        swapped(z,30)
        swapped(z,31)
        swapped(z,32)
        swapped(z,33)
        swapped(z,34)
        swapped(z,35)
        swapped(z,36)
        swapped(z,37)
        swapped(z,38)
        swapped(z,39)
        swapped(z,40)
        swapped(z,41)
        swapped(z,42)
        swapped(z,43)
        swapped(z,44)
        swapped(z,45)
        swapped(z,46)
        swapped(z,47)
        swapped(z,48)
        swapped(z,49)
        swapped(z,50)
        swapped(z,51)
        swapped(z,52)
        swapped(z,53)
        swapped(z,54)
        swapped(z,55)
        swapped(z,56)
        swapped(z,57)
        swapped(z,58)
        swapped(z,59)
        swapped(z,60)
        swapped(z,61)
        swapped(z,62)
        swapped(z,63)
        swapped(z,64)
        swapped(z,65)
        swapped(z,66)
        swapped(z,67)
        swapped(z,68)
        swapped(z,69)
        swapped(z,70)
        swapped(z,71)
        swapped(z,72)
        swapped(z,73)
        swapped(z,74)
        swapped(z,75)
        swapped(z,76)
        swapped(z,77)
        swapped(z,78)
        swapped(z,79)
        swapped(z,80)
        swapped(z,81)
        swapped(z,82)
        swapped(z,83)
        swapped(z,84)
        swapped(z,85)
        swapped(z,86)
        swapped(z,87)
        swapped(z,88)
        swapped(z,89)
        swapped(z,90)
        swapped(z,91)
        swapped(z,92)
        swapped(z,93)
        swapped(z,94)
        swapped(z,95)
        swapped(z,96)
        swapped(z,97)
        swapped(z,98)
        swapped(z,99)
        swapped(z,100)
        return z

    a = swappedinput(z)
    r = sortreversed(sortconvert(a))


    def swappedinputagain(r): #this function is swapped กลับไปตำแหน่งก่อนหน้าเพราะว่าต้องการจะเปลี่ยนกลับไปเป็นภาษาไทย
        def swapped(r,a):
            for i in range(0,len(r)):
                if len(r[i]) == a:
                    j = len(r[i])-1
                    k = j-1
                    while j >= 0 and j < len(r[i]):
                        d = r[i]
                        while k == j-1 and k >=0:
                            if d[k] in keysA and d[j] == 'n':
                                s = d[j]
                                d[j] = d[k]
                                d[k] = s
                                k-=1
                            if d[k] in keysA and d[j] == 'm':
                                s = d[j]
                                d[j] = d[k]
                                d[k] = s
                                k-=1
                            k-=1

                        j -=1
                elif a == 1:
                    break

            return r
        swapped(r,2)
        swapped(r,3)
        swapped(r,4)
        swapped(r,5)
        swapped(r,6)
        swapped(r,7)
        swapped(r,8)
        swapped(r,9)
        swapped(r,10)
        swapped(r,11)
        swapped(r,12)
        swapped(r,13)
        swapped(r,14)
        swapped(r,15)
        swapped(r,16)
        swapped(r,17)
        swapped(r,18)
        swapped(r,19)
        swapped(r,20)
        swapped(r,21)
        swapped(r,22)
        swapped(r,23)
        swapped(r,24)
        swapped(r,25)
        swapped(r,26)
        swapped(r,27)
        swapped(r,28)
        swapped(r,29)
        swapped(r,30)
        swapped(r,31)
        swapped(r,32)
        swapped(r,33)
        swapped(r,34)
        swapped(r,35)
        swapped(r,36)
        swapped(r,37)
        swapped(r,38)
        swapped(r,39)
        swapped(r,40)
        swapped(r,41)
        swapped(r,42)
        swapped(r,43)
        swapped(r,44)
        swapped(r,45)
        swapped(r,46)
        swapped(r,47)
        swapped(r,48)
        swapped(r,49)
        swapped(r,50)
        swapped(r,51)
        swapped(r,52)
        swapped(r,53)
        swapped(r,54)
        swapped(r,55)
        swapped(r,56)
        swapped(r,57)
        swapped(r,58)
        swapped(r,59)
        swapped(r,60)
        swapped(r,61)
        swapped(r,62)
        swapped(r,63)
        swapped(r,64)
        swapped(r,65)
        swapped(r,66)
        swapped(r,67)
        swapped(r,68)
        swapped(r,69)
        swapped(r,70)
        swapped(r,71)
        swapped(r,72)
        swapped(r,73)
        swapped(r,74)
        swapped(r,75)
        swapped(r,76)
        swapped(r,77)
        swapped(r,78)
        swapped(r,79)
        swapped(r,80)
        swapped(r,81)
        swapped(r,82)
        swapped(r,83)
        swapped(r,84)
        swapped(r,85)
        swapped(r,86)
        swapped(r,87)
        swapped(r,88)
        swapped(r,89)
        swapped(r,90)
        swapped(r,91)
        swapped(r,92)
        swapped(r,93)
        swapped(r,94)
        swapped(r,95)
        swapped(r,96)
        swapped(r,97)
        swapped(r,98)
        swapped(r,99)
        swapped(r,100)
        return r

    bb = swappedinputagain(r)

    h = []
    g = []
    def converttovalues(bb):
        for i in range(0,len(bb)):
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
        out_str= ""
        for x in w:
            goal.append(out_str.join(x))
        return goal


    result = lstostring(w)
    return result


def reduce(result):
    i = len(result) - 1
    while i >= 0 and i < len(result):
        if result[i] == result[i - 1]:
            del result[i]
        i -= 1
    return result

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active



if __name__ == '__main__':
    word = ["สิทฺธตฺถ","สาวกานํ","ปโรอุทปาทิ"]
    print(sortlistpalithai(word))

    # result = sortlistpalithai(word)
    # b = reduce(result)
    # k = [item for item in b]
    # for rows in zip(k):
    #     sheet.append(rows)
    #
    #
    # workbook.save(filename="C:\\Users\senio\Documents\\sort_tipitaka_allword.xlsx")

    # import sys
    # sys.stdout = open("C:\\Users\senio\Documents\\tipitaka.txt","w",encoding="utf-8")
    # print(k)
    # sys.stdout.close()



# เอเกกวณฺโณ อกฺขโร

