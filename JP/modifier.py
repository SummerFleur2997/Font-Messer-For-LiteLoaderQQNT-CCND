import random
from fontTools.ttLib import TTFont

CJK = []
for i in range(19968, 40960):
    hex_num = str(hex(i))
    CJK.append(hex_num)

JP_Hiragana = [
    "uni3041", "uni3042", "uni3043", "uni3044", "uni3045", "uni3046", "uni3047", "uni3048", "uni3049",
    "uni304A", "uni304B", "uni304C", "uni304D", "uni304E", "uni304F", "uni3050", "uni3051", "uni3052",
    "uni3053", "uni3054", "uni3055", "uni3056", "uni3057", "uni3058", "uni3059", "uni305A", "uni305B",
    "uni305C", "uni305D", "uni305E", "uni305F", "uni3060", "uni3061", "uni3062", "uni3063", "uni3064",
    "uni3065", "uni3066", "uni3067", "uni3068", "uni3069", "uni306A", "uni306B", "uni306C", "uni306D",
    "uni306E", "uni306F", "uni3070", "uni3071", "uni3072", "uni3073", "uni3074", "uni3075", "uni3076",
    "uni3077", "uni3078", "uni3079", "uni307A", "uni307B", "uni307C", "uni307D", "uni307E", "uni307F",
    "uni3080", "uni3081", "uni3082", "uni3083", "uni3084", "uni3085", "uni3086", "uni3087", "uni3088",
    "uni3089", "uni308A", "uni308B", "uni308C", "uni308D", "uni308E", "uni308F", "uni3090", "uni3091",
    "uni3092", "uni3093", "uni3094", "uni309D", "uni309E"]

JP_Katakana = [
    "uni30AB", "uni30AD", "uni30AF", "uni30B1", "uni30B3", "uni30B5", "uni30B7", "uni30B9", "uni30BB",
    "uni30BD", "uni30BF", "uni30C1", "uni30C6", "uni30C8", "uni30CA", "uni30CB", "uni30CC", "uni30CD",
    "uni30CE", "uni30CF", "uni30D2", "uni30D5", "uni30D8", "uni30DB", "uni30DE", "uni30DF", "uni30E0",
    "uni30E1", "uni30E2", "uni30E4", "uni30E6", "uni30E8", "uni30E9", "uni30EA", "uni30EB", "uni30EC",
    "uni30ED", "uni30EF", "uni30F0", "uni30F1", "uni30F2", "uni30F3"]
Latin = [
    "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def getXML():
    o_font = TTFont(r".\output\jp.TTF")
    o_font.saveXML(r".\output\jp.ttx", tables=["hhea"])


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

    for o in range(len(Latin)):
        Latin[o] = str(hex(ord(Latin[o])))

    for o in Latin:
        xml = f'<map code="{o}" name="{JP_Katakana[index]}"/>'
        f.write(xml + '\n')
        index = index + 1

    f.close()


if __name__ == "__main__":
    getXML()
