import os
import random
import subprocess
import xml.etree.ElementTree as ET

from index import *
from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import compress


declaration = '<?xml version="1.0" encoding="UTF-8"?>'


def getXML(name):
    o_font = TTFont(fr".\libs\{name}.TTF")
    o_font.saveXML(fr".\libs\{name}.ttx")


def COPY(item):
    temp = []
    for o in item:
        temp.append(o)
    return temp


def DeepShufferList(item, name):
    counter = 0
    temp = COPY(item)

    while True:
        random.shuffle(item)
        tag_stop = True
        for o in range(len(item)):
            if temp[o] == item[o]:
                tag_stop = False
                break
        counter += 1

        if tag_stop:
            print(f"Finished shuffling \"{name}\", tried {counter} time(s).")
            break


def XMLModifier(name: str, info: list[ET.Element]):
    XML = ET.parse(f"./libs/{name}.raw.ttx")
    root = XML.getroot()

    cmap = root.find('cmap')
    cmap_f = cmap.findall('cmap_format_4')

    for sub in cmap_f:
        temp = sub.attrib
        sub.clear()
        sub.extend(info)
        sub.attrib = temp

    XML.write(f"./libs/{name}.ttx", xml_declaration=True, encoding='utf-8')


def XMLAppend(self, index, name):
    new_element = ET.Element("map")
    new_element.attrib = {"code": f"{index}", "name": f"{name}"}
    self.append(new_element)


def START(namespace, info, keep_procedure=False):
    INIT()
    getXML(f"{namespace}.raw")
    XMLModifier(namespace, info)
    subprocess.run(f'ttx -o "libs\\{namespace}.ttf" "libs\\{namespace}.ttx"')
    compress(f"libs\\{namespace}.ttf", f"output\\{namespace}.woff2")

    if not keep_procedure:
        os.remove(f"libs\\{namespace}.raw.ttx")
        os.remove(f"libs\\{namespace}.ttf")
        os.remove(f"libs\\{namespace}.ttx")


if __name__ == "__main__":
    pass
