# pyqt-resource-helper
Setting icons, stylesheets of imported packages based on main module's path to prevent FileNotFoundError and improve convinience.

This can be used for PySide as well. But it is not written in requirements. Basically this is for PyQt.

## Requirements
PyQt6 >= 6.5.0

## Setup
`python -m pip install pyqt-resource-helper`

## Usage
```python
# set the icon
PyQtResourceHelper.setIcon([closeBtn], ['ico/close.png']) 
# set the style
PyQtResourceHelper.setStyleSheet([closeBtn], ['style/button.css'])
```
