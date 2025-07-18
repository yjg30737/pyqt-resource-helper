import inspect
import os
import re
import sys

from PyQt6.QtGui import QIcon


class PyQtResourceHelper:

    @staticmethod
    def setIcon(widgets: list, icon_paths: list):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        for i in range(len(widgets)):
            widgets[i].setIcon(QIcon(os.path.join(caller_path, icon_paths[i])))

    @staticmethod
    def setStyleSheet(widgets: list, style_sheets: list):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)

        def getStyleSheetOf(i):
            css_file_path = os.path.join(caller_path, style_sheets[i])
            css_file = open(css_file_path)
            css_code = css_file.read()
            css_file.close()
            return css_code

        if len(style_sheets) == 1:
            for i in range(len(widgets)):
                css_code = getStyleSheetOf(0)
                widgets[i].setStyleSheet(css_code)
        elif len(style_sheets) == 2:
            for i in range(len(widgets)):
                css_code = getStyleSheetOf(i % 2)
                widgets[i % 2].setStyleSheet(css_code)
        else:
            for i in range(len(widgets)):
                css_code = getStyleSheetOf(i)
                widgets[i].setStyleSheet(css_code)

    @staticmethod
    def addStyleToWidget(widget, tag, attr):
        style_sheet_text = widget.styleSheet()
        css_tag_regex = '\s*{\n?(.|\n)*?\n?}'
        ms = re.finditer(tag+css_tag_regex, style_sheet_text)
        lst = [m for m in ms]
        ms_len = len(lst)
        if ms_len:
            for m in lst:
                style_sheet_tag_to_changed = m.group()[:-1]
                style_sheet_text = style_sheet_text.replace(style_sheet_tag_to_changed, '')
                widget.setStyleSheet(style_sheet_tag_to_changed + attr + ';}' + widget.styleSheet()[m.span()[1]:])
        else:
            widget.setStyleSheet(style_sheet_text + tag + ' {' + attr + ';}')
