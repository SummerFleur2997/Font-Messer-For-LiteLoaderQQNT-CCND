import random
from index import *


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    for lst in {JP, CJK}:
        for o in lst:
            selectedLetter = random.choices(Latin_Cap, weights=Latin_weight)
            xml = f'<map code="{o}" name="{selectedLetter[0]}"/>'
            f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
