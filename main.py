from functions import *

GBK = COMMON[0:7]
KFC = COMMON


def geneXMLInfo_EN():
    xml_elements = []
    Latin_Cap_mirror = COPY(Latin_Cap)
    DeepShufferList(Number, "Number")
    DeepShufferList(Latin_Cap, "Latin Cap")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Cap[o])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Latin_Cap_mirror, weights=Latin_weight)[0]
            XMLAppend(xml_elements, o, selectedLetter)

    return xml_elements


def geneXMLInfo_GBK():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(Latin_Cap, "Latin Cap")

    Latin_Sml_mirror = COPY(Latin_Cap)
    for index in range(len(Latin_Sml_mirror)):
        Latin_Sml_mirror[index] = Latin_Sml_mirror[index].lower()

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Sml_mirror[o])

    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 7
            XMLAppend(xml_elements, o, GBK[index])
            counter = counter + 1

    return xml_elements


def geneXMLInfo_Greek():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(Greek_Cap, "Greek Cap")

    Greek_Cap_mirror = COPY(Greek_Cap)
    Greek_Cap_mirror.insert(16, 'Ξ')
    Greek_Cap_mirror.insert(25, 'Ψ')

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        oo = Greek_Sml.index(Greek_Cap_mirror[o].lower())
        XMLAppend(xml_elements, hex(0x41 + o), Greek_Cap_name[oo])
    for o in range(26):
        oo = Greek_Sml.index(Greek_Cap_mirror[o].lower())
        XMLAppend(xml_elements, hex(0x61 + o), Greek_Sml_name[oo])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Greek_Sml, weights=Greek_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = selectedLetter.upper()
                selectedLetter = Greek_Cap_name[Greek_Cap.index(selectedLetter)]
            else:
                selectedLetter = Greek_Sml_name[Greek_Sml.index(selectedLetter)]
            XMLAppend(xml_elements, o, selectedLetter)

    return xml_elements


def geneXMLInfo_JP():
    xml_elements = []
    DeepShufferList(Number, "Number")
    DeepShufferList(JP_Katakana, "Katakana")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(10):
        oo = str(hex(ord(Latin_vowel[o])))
        XMLAppend(xml_elements, oo, Katakana_vowel[o])
    for o in range(42):
        oo = str(hex(ord(Latin_conso[o])))
        XMLAppend(xml_elements, oo, JP_Katakana[o])

    for o in JP:
        JP_name = f"uni{o[2:].upper()}"
        XMLAppend(xml_elements, o, JP_name)

    counter = 0
    random.shuffle(JP_Hiragana)
    for o in CJK:
        index = counter % 86
        XMLAppend(xml_elements, o, JP_Hiragana[index])
        counter = counter + 1
        if counter % 86 == 0:
            random.shuffle(JP_Hiragana)

    return xml_elements


def geneXMLInfo_KFC():
    xml_elements = []

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Latin_Cap[o])
    for o in range(26):
        XMLAppend(xml_elements, hex(0x61 + o), Latin_Sml[o])

    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 12
            XMLAppend(xml_elements, o, KFC[index])
            counter = counter + 1

    return xml_elements


def geneXMLInfo_RUS():
    xml_elements = []
    DeepShufferList(Number, "Number")

    for o in range(10):
        XMLAppend(xml_elements, hex(0x30 + o), Number[o])

    random.shuffle(Russia_Cap_name)
    for o in range(26):
        XMLAppend(xml_elements, hex(0x41 + o), Russia_Cap_name[o])
    for o in range(26):
        oo = Russia_Sml_name.index(f"uni0{str(hex(int(Russia_Cap_name[o][-3:], 16) + 32))[-3:].upper()}")
        XMLAppend(xml_elements, hex(0x61 + o), Russia_Sml_name[oo])

    for lst in (JP, CJK):
        for o in lst:
            selectedLetter = random.choices(Russia_Sml, weights=Russia_weight)[0]
            if random.choices((True, False), weights=(0.2, 0.8))[0]:
                selectedLetter = str(hex(int(selectedLetter, 16) - 0x20))
                selectedLetter = Russia_Cap_name[Russia_Cap.index(selectedLetter)]
            else:
                selectedLetter = Russia_Sml_name[Russia_Sml.index(selectedLetter)]
            XMLAppend(xml_elements, o, selectedLetter)

    return xml_elements


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    START("EN", geneXMLInfo_EN())
    START("GBK", geneXMLInfo_GBK())
    START("Greek", geneXMLInfo_Greek())
    START("JP", geneXMLInfo_JP())
    START("KFC", geneXMLInfo_KFC())
    START("RUS", geneXMLInfo_RUS())
