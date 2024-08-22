import random
from index import *


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Russia_Sml, weights=Russia_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = str(hex(int(selectedLetter, 16) - 0x20))
                selectedLetter = Russia_Cap_name[Russia_Cap.index(selectedLetter)]
            else:
                selectedLetter = Russia_Sml_name[Russia_Sml.index(selectedLetter)]

            xml = f'      <map code="{o}" name="{selectedLetter}"/>'
            f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


def writeLatinInfo():
    f = open("log_Latin.xml", 'w')
    f.write("<cmap>\n")

    nn = 0
    temp = COPY(Number)
    while True:
        random.shuffle(Number)
        tag_stop = True
        for o in range(len(Number)):
            if temp[o] == Number[o]:
                tag_stop = False
                break

        nn += 1
        if tag_stop:
            print(f"Finished shuffling \"Number\", tried {nn} time(s).")
            break

    for o in range(10):
        xml = f'      <map code="{hex(0x30 + o)}" name="{Number[o]}"/>'
        f.write(xml + '\n')

    random.shuffle(Russia_Cap_name)
    for o in range(26):
        xml = f'      <map code="{hex(0x41 + o)}" name="{Russia_Cap_name[o]}"/>'
        f.write(xml + '\n')
    for o in range(26):
        oo = Russia_Sml_name.index(f"uni0{str(hex(int(Russia_Cap_name[o][-3:], 16) + 32))[-3:].upper()}")
        xml = f'      <map code="{hex(0x61 + o)}" name="{Russia_Sml_name[oo]}"/>'
        f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
