import random
from fontTools.ttLib import TTFont

CJK = []
for i in range(19968, 40960):
    hex_num = str(hex(i))
    CJK.append(hex_num)

Latin_Cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

Latin_Sml = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

JP = ["0x3041", "0x3042", "0x3043", "0x3044", "0x3045", "0x3046", "0x3047", "0x3048", "0x3049",
      "0x304a", "0x304b", "0x304c", "0x304d", "0x304e", "0x304f", "0x3050", "0x3051", "0x3052",
      "0x3053", "0x3054", "0x3055", "0x3056", "0x3057", "0x3058", "0x3059", "0x305a", "0x305b",
      "0x305c", "0x305d", "0x305e", "0x305f", "0x3060", "0x3061", "0x3062", "0x3063", "0x3064",
      "0x3065", "0x3066", "0x3067", "0x3068", "0x3069", "0x306a", "0x306b", "0x306c", "0x306d",
      "0x306e", "0x306f", "0x3070", "0x3071", "0x3072", "0x3073", "0x3074", "0x3075", "0x3076",
      "0x3077", "0x3078", "0x3079", "0x307a", "0x307b", "0x307c", "0x307d", "0x307e", "0x307f",
      "0x3080", "0x3081", "0x3082", "0x3083", "0x3084", "0x3085", "0x3086", "0x3087", "0x3088",
      "0x3089", "0x308a", "0x308b", "0x308c", "0x308d", "0x308e", "0x308f", "0x3090", "0x3091",
      "0x3092", "0x3093", "0x3094", "0x309d", "0x309e", "0x30a1", "0x30a2", "0x30a3", "0x30a4",
      "0x30a5", "0x30a6", "0x30a7", "0x30a8", "0x30a9", "0x30aa", "0x30ab", "0x30ac", "0x30ad",
      "0x30ae", "0x30af", "0x30b0", "0x30b1", "0x30b2", "0x30b3", "0x30b4", "0x30b5", "0x30b6",
      "0x30b7", "0x30b8", "0x30b9", "0x30ba", "0x30bb", "0x30bc", "0x30bd", "0x30be", "0x30bf",
      "0x30c0", "0x30c1", "0x30c2", "0x30c3", "0x30c4", "0x30c5", "0x30c6", "0x30c7", "0x30c8",
      "0x30c9", "0x30ca", "0x30cb", "0x30cc", "0x30cd", "0x30ce", "0x30cf", "0x30d0", "0x30d1",
      "0x30d2", "0x30d3", "0x30d4", "0x30d5", "0x30d6", "0x30d7", "0x30d8", "0x30d9", "0x30da",
      "0x30db", "0x30dc", "0x30dd", "0x30de", "0x30df", "0x30e0", "0x30e1", "0x30e2", "0x30e3",
      "0x30e4", "0x30e5", "0x30e6", "0x30e7", "0x30e8", "0x30e9", "0x30ea", "0x30eb", "0x30ec",
      "0x30ed", "0x30ee", "0x30ef", "0x30f0", "0x30f1", "0x30f2", "0x30f3", "0x30f4", "0x30f5",
      "0x30f6", "0x30f7", "0x30f8", "0x30f9", "0x30fa", "0x30fc", "0x30fd", "0x30fe"]

GBK = ["uni4E00", "uni4E01", "uni4E02", "uni4E03", "uni4E04", "uni4E05", "uni4E06"]


def getXML():
    o_font = TTFont(r".\output\GBK.TTF")
    o_font.saveXML(r".\output\GBK.ttx")


def writeInfo():
    f = open("log_cjk.xml", 'w')
    Latin_Cap_bak = []
    Latin_Sml_bak = []
    for o in range(26):
        Latin_Cap_bak.append(Latin_Cap[o])
        Latin_Sml_bak.append(Latin_Sml[o])

    random.shuffle(Latin_Cap_bak)
    random.shuffle(Latin_Sml_bak)

    while True:
        p = 0
        for o in range(26):
            if Latin_Cap_bak[o] == Latin_Cap[o] or Latin_Sml_bak[o] == Latin_Sml[o]:
                p = p + 1

        if p == 0:
            break
        else:
            random.shuffle(Latin_Cap_bak)
            random.shuffle(Latin_Sml_bak)

    for o in range(65, 91):
        xml = f'<map code="{str(hex(o))}" name="{Latin_Cap_bak[o - 65]}"/>'
        f.write(xml + '\n')

    for o in range(97, 123):
        xml = f'<map code="{str(hex(o))}" name="{Latin_Sml_bak[o - 97]}"/>'
        f.write(xml + '\n')

    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 7
            xml = f'<map code="{o}" name="{GBK[index]}"/>'
            f.write(xml + '\n')
            counter = counter + 1

    f.close()


if __name__ == "__main__":
    writeInfo()
