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
        if len(style_sheets) == 1:
            for i in range(len(widgets)):
                css_file_path = os.path.join(caller_path, style_sheets[0])
                css_file = open(css_file_path)
                css_code = css_file.read()
                css_file.close()
                widgets[i].setStyleSheet(css_code)
        elif len(style_sheets) == 2:
            caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
            for i in range(len(widgets)):
                css_file_path = os.path.join(caller_path, style_sheets[i % 2])
                css_file = open(css_file_path)
                css_code = css_file.read()
                css_file.close()
                widgets[i].setStyleSheet(css_code)
        else:
            caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
            for i in range(len(widgets)):
                css_file_path = os.path.join(caller_path, style_sheets[i])
                css_file = open(css_file_path)
                css_code = css_file.read()
                css_file.close()
                widgets[i].setStyleSheet(css_code)