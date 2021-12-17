# pyqt-resource-helper
Setting icons, stylesheets of imported packages based on main module to prevent FileNotFoundError

## Requirements
PyQt5 >= 5.8

## Usage
```python
# set the icon
PyQtResourceHelper.setIcon([closeBtn], ['ico/close.png']) 
# set the style
PyQtResourceHelper.setStyleSheet([closeBtn], ['style/button.css'])
```
