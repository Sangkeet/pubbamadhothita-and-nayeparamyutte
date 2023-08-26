# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

from compose_yoga import *

def romantothai(name2):
    name2 = name2.lower()
    Alphabeticsroman = {
        'a':'อ',
        'ā':'อา',
        'i':'อิ',
        'ī':'อี',
        'u':'อุ',
        'ū':'อู',
        'e':'เอ',
        'o':'โอ',
        'k':'กฺ',
        'kh':'ขฺ',
        'g':'คฺ',
        'gh':'ฆฺ',
        'ṅ':'งฺ',
        'c':'จฺ',
        'ch':'ฉฺ',
        'j':'ชฺ',
        'jh':'ฌฺ',
        'ñ':'ญฺ',
        'ṭ':'ฏฺ',
        'ṭh':'ฐฺ',
        'ḍ':'ฑฺ',
        'ḍh':'ฒฺ',
        'ṇ':'ณฺ',
        't':'ตฺ',
        'th':'ถฺ',
        'd':'ทฺ',
        'dh':'ธฺ',
        'n':'นฺ',
        'p':'ปฺ',
        'ph':'ผฺ',
        'b':'พฺ',
        'bh':'ภฺ',
        'm':'มฺ',
        'y':'ยฺ',
        'r':'รฺ',
        'l':'ลฺ',
        'v':'วฺ',
        's':'สฺ',
        'h':'หฺ',
        'ḷ':'ฬฺ',
        'aṃ':'อํ',
        'iṃ':'อิํ',
        'uṃ':'อุํ',
        'sp':' '
    }

    def lstostring(w):
        g = []
        out_str= ""
        for x in w:
            g.append(out_str.join(x))
        return g


    def listtostring(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1


    def sortreversed(y):
        i = []
        for a in range(0, len(y)):
            i.append(y[-1 - a])
        return i



    sara = ['a','ā','i','ī','u','ū','e','o','aṃ','iṃ','uṃ']
    sithila = ['k','g','c','j','ṭ','ḍ','t','d','p','b']
    avagga = ['y','r','l','v','s','h','ḷ']
    nasika = ['ṅ','ñ','ṇ','n','m']
    space = ' '




    name3 = sortreversed(name2)

    sadda = []
    j = 0
    while j>=0 and j<len(name3):
        if name3[j]=='ṃ':
            sadda.append(name3[j+1]+name3[j])
            j = j+1
        elif name3[j]=='h' and name3[j+1] in sithila:
            sadda.append(name3[j+1]+name3[j])
            j = j+1
        elif name3[j] in sara:
            sadda.append(name3[j])
        elif name3[j] in sithila+avagga+nasika:
            sadda.append(name3[j])
        else:
            sadda.append('sp')
        j = j+1

    sadda2 = sortreversed(sadda)
    sadda3 = []
    for item in sadda2:
        sadda3.append(Alphabeticsroman[item])


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


    print(sadda3)
    s = sadda3
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

    return sortreversed(lstostring(wording))



def thaitoroman(word):
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

    def isolate(word):
        iso = []
        z = len(word)
        consonant_para = "ํ"
        vowel_sound = "อ"
        vowel_textpubba = ["า", "ิ", "ี", "ุ", "ู"]
        vowel_rassa = ["ิ","ุ"]
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
        elif x in range(0,z):
            while x>=0 and x<z:
                if y[z-2] in consonant_palithai and y[z-1] in consonant_para:
                    iso.append(y[z-1])
                    iso.append(vowel_sound)
                    iso.append(y[z-2] + press_vowel)
                    z = z-1
                elif y[z-2] in vowel_textpara and y[z-1] in consonant_palithai:
                    iso.append(y[z-2]+vowel_sound)
                    iso.append(y[z - 1] + press_vowel)
                    z = z-1
                elif y[z-3] in consonant_palithai and y[z-2] in vowel_textpubba and y[z-1] in consonant_para:
                    iso.append(y[z-1])
                    iso.append(vowel_sound + y[z-2])
                    iso.append(y[z-3] + press_vowel)
                    z = z-2
                elif y[z-2] in consonant_palithai and y[z-1] in press_vowel:
                    iso.append(y[z-2]+y[z-1])
                    z = z-1
                elif y[z-2] in consonant_palithai and y[z - 1] in vowel_textpubba:
                    iso.append(vowel_sound + y[z-1])
                    iso.append(y[z-2] + press_vowel)
                    z = z-1
                elif y[z-1] in consonant_palithai:
                    iso.append(vowel_sound)
                    iso.append(y[z-1] + press_vowel)
                if y[z-1] in space:
                    iso.append(space)
                if y[z - 2] in vowel_textpara and y[z - 1] in vowel_sound:
                    iso.append(y[z - 2] + vowel_sound)
                    z = z - 1
                elif y[z - 2] in vowel_sound and y[z - 1] in consonant_para:
                    iso.append(y[z - 2] + y[z - 1])
                    z = z - 1
                elif y[z-1] in vowel_sound:
                    iso.append(y[z-1])
                elif y[z - 2] in vowel_sound and y[z - 1] in vowel_textpubba:
                    iso.append(y[z-2] + y[z-1])
                    z = z - 1
                elif y[z - 3] in vowel_sound and y[z - 2] in vowel_textpubba and y[z - 1] in consonant_para:
                    iso.append(y[z-3] + y[z-2])
                    iso.append(y[z-1])
                    z = z - 2

                z = z-1


        return iso

    xor = convertcommand(word)
    nor = converttovalues(lstostring(xor))
    kor = lstostring(nor)
    sadda = sortreversed(isolate(kor))

    sound = []
    for item in sadda:
        sound.append(toroman[item])

    k = 0
    if k in range(0,len(sound[0])):
        x = sound[0]
        if len(sound[0]) == 2:
            y = x[k].upper()+x[k+1]
        elif len(sound[0]) == 1:
            y = x[k].upper()

        changeroman = []
        changeroman.append(y)
        for item2 in range(1,len(sadda)):
            changeroman.append(sound[item2])

        str1 = ""
        for w in changeroman:
            str1 = str1+w

        return str1


def thaitosinhala(word):
    sinhala = {
        'อ':'අ',
        'อา':'ආ',
        'อิ':'ඉ',
        'อี':'ඊ',
        'อุ':'උ',
        'อู':'ඌ',
        'เอ':'එ',
        'โอ':'ඔ',
        'ก':'ක',
        'กํ':'කං',
        'กา':'කා',
        'กิ':'කි',
        'กิํ':'කිං',
        'กี':'කී',
        'กุ':'කු',
        'กุํ':'කුං',
        'กู':'කූ',
        'เก':'කෙ',
        'โก':'කො',
        'กฺ':'ක්',
        'ข':'ඛ',
        'ขํ':'ඛං',
        'ขา':'ඛා',
        'ขิ':'ඛි',
        'ขิํ':'ඛිං',
        'ขี':'ඛී',
        'ขุ':'ඛු',
        'ขุํ':'ඛුං',
        'ขู':'ඛූ',
        'เข':'ඛෙ',
        'โข':'ඛො',
        'ขฺ':'බ්',
        'ค':'ග',
        'คํ':'ගං',
        'คา':'ගා',
        'คิ':'ගි',
        'คิํ':'ගිං',
        'คี':'ගී',
        'คุ':'ගු',
        'คุํ':'ගුං',
        'คู':'ගූ',
        'เค':'ගෙ',
        'โค':'ගො',
        'คฺ':'ග්',
        'ฆ':'ඝ',
        'ฆํ':'ඝං',
        'ฆา':'ඝා',
        'ฆิ':'ඝි',
        'ฆิํ':'ඝිං',
        'ฆี':'ඝී',
        'ฆุ':'ඝු',
        'ฆุํ':'ඝුං',
        'ฆู':'ඝූ',
        'เฆ':'ඝෙ',
        'โฆ':'ඝො',
        'ฆฺ':'ඝ්',
        'ง':'ඞ',
        'งํ':'ඞං',
        'งา':'ඞා',
        'งิ':'ඞි',
        'งิํ':'ඞිං',
        'งี':'ඞී',
        'งุ':'ඞු',
        'งุํ':'ඞුං',
        'งู':'ඞූ',
        'เง':'ඞෙ',
        'โง':'ඞො',
        'งฺ':'ඞ්',
        'จ':'ච',
        'จํ':'චං',
        'จา':'චා',
        'จิ':'චි',
        'จิํ':'චිං',
        'จี':'චී',
        'จุ':'චු',
        'จุํ':'චුං',
        'จู':'චූ',
        'เจ':'චෙ',
        'โจ':'චො',
        'จฺ':'ච්',
        'ฉ':'ඡ',
        'ฉํ':'ඡං',
        'ฉา':'ඡා',
        'ฉิ':'ඡි',
        'ฉิํ':'ඡිං',
        'ฉี':'ඡී',
        'ฉุ':'ඡු',
        'ฉุํ':'ඡුං',
        'ฉู':'ඡූ',
        'เฉ':'ඡෙ',
        'โฉ':'ඡො',
        'ฉฺ':'ඡ්',
        'ช':'ජ',
        'ชํ':'ජං',
        'ชา':'ජා',
        'ชิ':'ජි',
        'ชิํ':'ජිං',
        'ชี':'ජී',
        'ชุ':'ජු',
        'ชุํ':'ජුං',
        'ชู':'ජූ',
        'เช':'ජෙ',
        'โช':'ජො',
        'ชฺ':'ජ්',
        'ฌ':'ඣ',
        'ฌํ':'ඣං',
        'ฌา':'ඣා',
        'ฌิ':'ඣි',
        'ฌิํ':'ඣිං',
        'ฌี':'ඣී',
        'ฌุ':'ඣු',
        'ฌุํ':'ඣුං',
        'ฌู':'ඣූ',
        'เฌ':'ඣෙ',
        'โฌ':'ඣො',
        'ฌฺ':'ඣ්',
        'ญ':'ඤ',
        'ญํ':'ඤං',
        'ญา':'ඤා',
        'ญิ':'ඤි',
        'ญิํ':'ඤිං',
        'ญี':'ඤී',
        'ญุ':'ඤු',
        'ญุํ':'ඤුං',
        'ญู':'ඤූ',
        'เญ':'ඤෙ',
        'โญ':'ඤො',
        'ญฺ':'ඤ්',
        'ฏ':'ට',
        'ฏํ':'ටං',
        'ฏา':'ටා',
        'ฏิ':'ටි',
        'ฏิํ':'ටිං',
        'ฏี':'ටී',
        'ฏุ':'ටු',
        'ฏุํ':'ටුං',
        'ฏู':'ටූ',
        'เฏ':'ටෙ',
        'โฏ':'ටො',
        'ฏฺ':'ට්',
        'ฐ':'ඨ',
        'ฐํ':'ඨං',
        'ฐา':'ඨා',
        'ฐิ':'ඨි',
        'ฐิํ':'ඨිං',
        'ฐี':'ඨී',
        'ฐุ':'ඨු',
        'ฐุํ':'ඨුං',
        'ฐู':'ඨූ',
        'เฐ':'ඨෙ',
        'โฐ':'ඨො',
        'ฐฺ':'ඨ්',
        'ฑ':'ඩ',
        'ฑํ':'ඩං',
        'ฑา':'ඩා',
        'ฑิ':'ඩි',
        'ฑิํ':'ඩිං',
        'ฑี':'ඩී',
        'ฑุ':'ඩු',
        'ฑุํ':'ඩුං',
        'ฑู':'ඩූ',
        'เฑ':'ඩෙ',
        'โฑ':'ඩො',
        'ฑฺ':'ඩ්',
        'ฒ':'ඪ',
        'ฒํ':'ඪං',
        'ฒา':'ඪා',
        'ฒิ':'ඪි',
        'ฒิํ':'ඪිං',
        'ฒี':'ඪී',
        'ฒุ':'ඪු',
        'ฒุํ':'ඪුං',
        'ฒู':'ඪූ',
        'เฒ':'ඪෙ',
        'โฒ':'ඪො',
        'ฒฺ':'ඪ්',
        'ณ':'ණ',
        'ณํ':'ණං',
        'ณา':'ණා',
        'ณิ':'ණි',
        'ณิํ':'ණිං',
        'ณี':'ණී',
        'ณุ':'ණු',
        'ณุํ':'ණුං',
        'ณู':'ණූ',
        'เณ':'ණෙ',
        'โณ':'ණො',
        'ณฺ':'ණ්',
        'ต':'ත',
        'ตํ':'තං',
        'ตา':'තා',
        'ติ':'ති',
        'ติํ':'තිං',
        'ตี':'තී',
        'ตุ':'තු',
        'ตุํ':'තුං',
        'ตู':'තූ',
        'เต':'තෙ',
        'โต':'තො',
        'ตฺ':'ත්',
        'ถ':'ථ',
        'ถํ':'ථං',
        'ถา':'ථා',
        'ถิ':'ථි',
        'ถิํ':'ථිං',
        'ถี':'ථී',
        'ถุ':'ථු',
        'ถุํ':'ථුං',
        'ถู':'ථූ',
        'เถ':'ථෙ',
        'โถ':'ථො',
        'ถฺ':'ථ්',
        'ท':'ද',
        'ทํ':'දං',
        'ทา':'දා',
        'ทิ':'දි',
        'ทิํ':'දිං',
        'ที':'දී',
        'ทุ':'දු',
        'ทุํ':'දුං',
        'ทู':'දූ',
        'เท':'දෙ',
        'โท':'දො',
        'ทฺ':'ද්',
        'ธ':'ධ',
        'ธํ':'ධං',
        'ธา':'ධා',
        'ธิ':'ධි',
        'ธิํ':'ධිං',
        'ธี':'ධී',
        'ธุ':'ධු',
        'ธุํ':'ධුං',
        'ธู':'ධූ',
        'เธ':'ධෙ',
        'โธ':'ධො',
        'ธฺ':'ධ්',
        'น':'න',
        'นํ':'නං',
        'นา':'නා',
        'นิ':'නි',
        'นิํ':'නිං',
        'นี':'නී',
        'นุ':'නු',
        'นุํ':'නුං',
        'นู':'නූ',
        'เน':'නෙ',
        'โน':'නො',
        'นฺ':'න්',
        'ป':'ප',
        'ปํ':'පං',
        'ปา':'පා',
        'ปิ':'පි',
        'ปิํ':'පිං',
        'ปี':'පී',
        'ปุ':'පු',
        'ปุํ':'පුං',
        'ปู':'පූ',
        'เป':'පෙ',
        'โป':'පො',
        'ปฺ':'ප්',
        'ผ':'ඵ',
        'ผํ':'ඵං',
        'ผา':'ඵා',
        'ผิ':'ඵි',
        'ผิํ':'ඵිං',
        'ผี':'ඵී',
        'ผุ':'ඵු',
        'ผุํ':'ඵුං',
        'ผู':'ඵූ',
        'เผ':'ඵෙ',
        'โผ':'ඵො',
        'ผฺ':'ඵ්',
        'พ':'බ',
        'พํ':'බං',
        'พา':'බා',
        'พิ':'බි',
        'พิํ':'බිං',
        'พี':'බී',
        'พุ':'බු',
        'พุํ':'බුං',
        'พู':'බූ',
        'เพ':'බෙ',
        'โพ':'බො',
        'พฺ':'බ්',
        'ภ':'භ',
        'ภํ':'භං',
        'ภา':'භා',
        'ภิ':'භි',
        'ภิํ':'භිං',
        'ภี':'භී',
        'ภุ':'භු',
        'ภุํ':'භුං',
        'ภู':'භූ',
        'เภ':'භෙ',
        'โภ':'භො',
        'ภฺ':'භ්',
        'ม':'ම',
        'มํ':'මං',
        'มา':'මා',
        'มิ':'මි',
        'มิํ':'මිං',
        'มี':'මී',
        'มุ':'මු',
        'มุํ':'මුං',
        'มู':'මූ',
        'เม':'මෙ',
        'โม':'මො',
        'มฺ':'ම්',
        'ย':'ය',
        'ยํ':'යං',
        'ยา':'යා',
        'ยิ':'යි',
        'ยิํ':'යිං',
        'ยี':'යී',
        'ยุ':'යු',
        'ยุํ':'යුං',
        'ยู':'යූ',
        'เย':'යෙ',
        'โย':'යො',
        'ยฺ':'ය්',
        'ร':'ර',
        'รํ':'රං',
        'รา':'රා',
        'ริ':'රි',
        'ริํ':'රිං',
        'รี':'රී',
        'รุ':'රු',
        'รุํ':'රුං',
        'รู':'රූ',
        'เร':'රෙ',
        'โร':'රො',
        'รฺ':'ර්',
        'ล':'ල',
        'ลํ':'ලං',
        'ลา':'ලා',
        'ลิ':'ලි',
        'ลิํ':'ලිං',
        'ลี':'ලී',
        'ลุ':'ලු',
        'ลุํ':'ලුං',
        'ลู':'ලූ',
        'เล':'ලෙ',
        'โล':'ලො',
        'ลฺ':'ල්',
        'ว':'ව',
        'วํ':'වං',
        'วา':'වා',
        'วิ':'වි',
        'วิํ':'විං',
        'วี':'වී',
        'วุ':'වු',
        'วุํ':'වුං',
        'วู':'වූ',
        'เว':'වෙ',
        'โว':'වො',
        'วฺ':'ව්',
        'ส':'ස',
        'สํ':'සං',
        'สา':'සා',
        'สิ':'සි',
        'สิํ':'සිං',
        'สี':'සී',
        'สุ':'සු',
        'สุํ':'සුං',
        'สู':'සූ',
        'เส':'සෙ',
        'โส':'සො',
        'สฺ':'ස්',
        'ห':'හ',
        'หํ':'හං',
        'หา':'හා',
        'หิ':'හි',
        'หิํ':'හිං',
        'หี':'හී',
        'หุ':'හු',
        'หุํ':'හුං',
        'หู':'හූ',
        'เห':'හෙ',
        'โห':'හො',
        'หฺ':'හ්',
        'ฬ':'ළ',
        'ฬํ':'ළං',
        'ฬา':'ළා',
        'ฬิ':'ළි',
        'ฬิํ':'ළිං',
        'ฬี':'ළී',
        'ฬุ':'ළු',
        'ฬุํ':'ළුං',
        'ฬู':'ළූ',
        'เฬ':'ළෙ',
        'โฬ':'ළො',
        'ฬฺ':'ළ්',
        ' ':' ',
        '\n':'\n'
    }

    sound_a = ['า','ิ','ี','ุ','ู','ํ','ฺ']
    sound_b = ['เ','โ']

    x = 0
    kam = []
    word_a = []
    for item in word:
        for i in item:
            word_a.append(i)


    t = len(word_a)
    while x >= 0 and x < t:
        if word_a[t-1] in sound_a and word_a[t-2] in sound_a:
            kam.append(word_a[t-3]+word_a[t-2]+word_a[t-1])
            t = t-2
        elif word_a[t-1] in sound_a:
            kam.append(word_a[t-2]+word_a[t-1])
            t = t-1
        elif word_a[t-2] in sound_b:
            kam.append(word_a[t-2]+word_a[t-1])
            t = t-1
        elif word_a[t-1] not in sound_a and word[t-2] not in sound_b:
            kam.append(word_a[t-1])

        t = t-1


    def sortreversed(y):
        i = []
        for a in range(0,len(y)):
            i.append(y[-1-a])
        return i


    kam_a = sortreversed(kam)
    x = 0
    sinh = []
    while x >= 0 and x < len(kam_a):
        sinh.append(sinhala[kam_a[x]])
        x = x+1

    def listtostring(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    return listtostring(sinh)
