#!/usr/bin/env python3

"""
Custom text in the main program - mimetype
"""

from PyQt5.QtCore import (QFileInfo,QMimeDatabase)

def fct(fpath):
    try:
        fileInfo = QFileInfo(fpath)
        imime = QMimeDatabase().mimeTypeForFile(fpath, QMimeDatabase.MatchDefault)
        if imime:
            return ["Type", imime.name()]
        else:
            return ["Type", "Unknown"]
    except:
        return ["Type", "Unknown"]
