import random
from index import *
import unicodedata


def RemoveAccents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def GetWeight():
    weight = []
    letter = []
    with open(".\\sample.txt") as f:
        greek = f.read()

    greek = greek.lower()
    greek = RemoveAccents(greek)
    for o in greek:
        if o not in letter:
            letter.append(o)
            weight.append(1)
        else:
            index = letter.index(o)
            weight[index] += 1
    print(letter, len(letter))
    print(weight, len(weight))


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Greek_Sml, weights=Greek_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = selectedLetter.upper()
                selectedLetter = Greek_Cap_name[Greek_Cap.index(selectedLetter)]
            else:
                selectedLetter = Greek_Sml_name[Greek_Sml.index(selectedLetter)]

            xml = f'      <map code="{o}" name="{selectedLetter}"/>'
            f.write(xml + '\n')

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
