import os

from PyQt5.QtGui import QIcon


class PyQtResourceHelper:

    @staticmethod
    def setIcon(widgets: list, icon_paths: list):
        rel_path = os.path.relpath(__file__, os.getcwd())
        for i in range(len(widgets)):
            widgets[i].setIcon(QIcon(os.path.join(os.path.dirname(rel_path), icon_paths[i])))

    @staticmethod
    def setStyleSheet(widgets: list, style_sheets: list):
        rel_path = os.path.relpath(__file__, os.getcwd())
        for i in range(len(widgets)):
            css_file_path = os.path.join(os.path.dirname(rel_path), style_sheets[i])
            css_file = open(css_file_path)
            css_code = css_file.read()
            css_file.close()
            widgets[i].setStyleSheet(css_code)
