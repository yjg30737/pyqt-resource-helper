# pyqt-resource-helper
Setting icons, stylesheets of imported packages based on main module's path to prevent FileNotFoundError

## Requirements
PyQt5 >= 5.8

## Setup
`pip3 install pyqt-resource-helper`

## Usage
```python
# set the icon
PyQtResourceHelper.setIcon([closeBtn], ['ico/close.png']) 
# set the style
PyQtResourceHelper.setStyleSheet([closeBtn], ['style/button.css'])
```
