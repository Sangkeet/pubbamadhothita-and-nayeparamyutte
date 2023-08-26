def roman(word):
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


if __name__ == '__main__':
    word = "อํส"
    print(roman(word))