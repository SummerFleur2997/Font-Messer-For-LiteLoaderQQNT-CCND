import random
from index import *

GBK = COMMON[0:7]


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 7
            xml = f'<map code="{o}" name="{GBK[index]}"/>'
            f.write(xml + '\n')
            counter = counter + 1

    f.write("</cmap>")
    f.close()


def writeLatinInfo():
    f = open("log_latin.xml", 'w')
    f.write("<cmap>\n")

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

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
