# pyqt-resource-helper
Setting icons, stylesheets of imported packages based on main module's path to prevent FileNotFoundError

Can be used in PyQt5, PyQt6, PySide2, PySide6.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-resource-helper`

## Included Packages
* <a href="https://github.com/spyder-ide/qtpy.git">qtpy</a> - Make this module support not only PyQt5 but also PyQt6, PySide2, PySide6

## Usage
```python
# set the icon
PyQtResourceHelper.setIcon([closeBtn], ['ico/close.png']) 
# set the style
PyQtResourceHelper.setStyleSheet([closeBtn], ['style/button.css'])
```
