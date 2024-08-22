import random
from index import *


def writeCJKInfo():
    counter = 0
    random.shuffle(JP_Hiragana)
    f = open("log_cjk.xml", 'w')

    for o in CJK:
        index = counter % 86
        xml = f'<map code="{o}" name="{JP_Hiragana[index]}"/>'
        f.write(xml + '\n')

        counter = counter + 1
        if counter % 86 == 0:
            random.shuffle(JP_Hiragana)

    f.close()


def writeLatinInfo():
    index = 0
    random.shuffle(JP_Katakana)
    f = open("log_latin.xml", 'w')
    f.write("<cmap>\n")

    for o in range(len(Latin)):
        Latin[o] = str(hex(ord(Latin[o])))

    for o in Latin:
        xml = f'<map code="{o}" name="{JP_Katakana[index]}"/>'
        f.write(xml + '\n')
        index = index + 1

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
