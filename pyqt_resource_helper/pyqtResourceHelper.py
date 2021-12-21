import os, inspect, sys

from PyQt5.QtGui import QIcon


class PyQtResourceHelper:

    @staticmethod
    def setIcon(widgets: list, icon_paths: list):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        for i in range(len(widgets)):
            widgets[i].setIcon(QIcon(os.path.join(caller_path, icon_paths[i])))

    @staticmethod
    def setStyleSheet(widgets: list, style_sheets: list):
        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)

        def setStyleSheetOf(i):
            css_file_path = os.path.join(caller_path, style_sheets[i])
            css_file = open(css_file_path)
            css_code = css_file.read()
            css_file.close()
            widgets[i].setStyleSheet(css_code)

        if len(style_sheets) == 1:
            for i in range(len(widgets)):
                setStyleSheetOf(0)
        elif len(style_sheets) == 2:
            for i in range(len(widgets)):
                setStyleSheetOf(i % 2)
        else:
            for i in range(len(widgets)):
                setStyleSheetOf(i)