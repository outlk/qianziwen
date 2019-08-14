#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "gzshen"

import json

with open(r"..\text.json", encoding="utf-8") as fp:
    allx = json.load(fp)

with open("qzw.tex", mode="w", encoding="utf-8") as fp:
    for i, x in enumerate(allx):
        py = x["pinyin"]
        txt = x["text"]
        com = x["comment"]
        py = ["{{\\pinyinzh \\bfseries {}}}".format(x) for x in py]
        txt = ["{{\\wenzizh \\bfseries {}}}".format(x) for x in txt]
        pyout = "{} & & {} \\\\".format(
            " & ".join(py[0:4]), " & ".join(py[4:8]))
        # print(pyout)
        fp.write(pyout + "\n")
        txtout = "{} & & {} \\\\".format(
            " & ".join(txt[0:4]), " & ".join(txt[4:8]))
        # print(txtout)
        fp.write(txtout + "\n")
        if py[8:12]:
            pyout = "{} & & {} \\\\".format(
                " & ".join(py[8:12]), " & ".join(py[12:16]))
            # print(pyout)
            fp.write(pyout + "\n")
            txtout = "{} & & {} \\\\".format(
                " & ".join(txt[8:12]), " & ".join(txt[12:16]))
            # print(txtout)
            fp.write(txtout + "\n")

        comout = "\\multicolumn{{9}}{{p{{0.95\\textwidth}}}}{{\\zhushizh {}}}\\\\".format(
            com)
        # print(comout)

        fp.write("\\\\\n")
        fp.write(comout + "\n")
        if (i+1) % 2 == 0:
            fp.write("\\newpage\n")
        elif (i+1) % 2 == 1:
            fp.write("\\\\\n")


with open("qzw_all.tex", mode="w", encoding="utf-8") as fp:
    for i, x in enumerate(allx):
        txt = x["text"]
        sens = len(txt)//4
        txt = "~".join(["".join(txt[i:i+4]) for i in range(0, len(txt),4)])
        # txt = "~".join(txt)
        print(txt)
        if (i+1) % 2 == 0:
            fp.write(txt + "\\\\\n")
        elif (i+1) % 2 == 1:
            if sens == 2:
                fp.write(txt)
            elif sens == 4:
                fp.write(txt+"~")

with open("qzw_all_kindle.tex", mode="w", encoding="utf-8") as fp:
    for i, x in enumerate(allx):
        txt = x["text"]
        sens = len(txt)//4
        txt = "~".join(["".join(txt[i:i+4]) for i in range(0, len(txt),4)])
        # txt = "~".join(txt)
        print(txt)
        fp.write(txt + "\\\\\n")
