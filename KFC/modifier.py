from index import *

KFC = COMMON


def writeCJKInfo():
    f = open("log_cjk.xml", 'w')
    f.write("<cmap>\n")

    for lst in [JP, CJK]:
        counter = 0
        for o in lst:
            index = counter % 12
            xml = f'<map code="{o}" name="{KFC[index]}"/>'
            f.write(xml + '\n')
            counter = counter + 1

    f.write("</cmap>")
    f.close()


if __name__ == "__main__":
    pass
