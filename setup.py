from setuptools import setup, find_packages

setup(
    name='pyqt-resource-helper',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='Setting icons, stylesheets of imported packages based on main module to prevent FileNotFoundError',
    url='https://github.com/yjg30737/pyqt-resource-helper.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)