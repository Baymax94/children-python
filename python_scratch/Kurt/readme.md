# 使用Kurt学习scratch和python
源自[Kurt](https://en.scratch-wiki.info/wiki/Kurt)——用于读取/写入[Scratch项目文件](https://en.scratch-wiki.info/wiki/Scratch_File_Format)  

## Kurt_Python
Project description
### kurt
Kurt is a Python library for working with Scratch project files.  
It supports both Scratch 1.4 and Scratch 2.0 with a single Pythonic interface, and it's extensible to support new file formats for Scratch mods (such as [Snap!](http://snap.berkeley.edu/)).  
It also includes a parser for converting plain text into Scratch blocks.  
Example uses:  
* converting Scratch 2.0 projects back to 1.4
* importing thousands of images into Scratch
* importing midi files as play note blocks
* importing font files as costumes
* parsing text to Scratch blocks
* analysing projects  

*[Scratch](http://scratch.mit.edu/) is created by the Lifelong Kindergarten Group at the MIT Media Lab.*
#### Installation
With a proper python environment (one which has [pip](http://www.pip-installer.org/en/latest/installing.html) available), simply run:
```
pip install kurt
```
Or using `easy_install`:
```
easy_install kurt
```
Or download the compressed archive [from PyPI](http://pypi.python.org/pypi/kurt), extract it, and inside it run:
```
python setup.py install
```
#### Requirements
Requires **Python 2.7**. Doesn't support Python 3.  
The installation methods above will automatically install kurt and its dependencies. To do a manual install instead, you need:
* **[Construct](http://github.com/construct/construct/tree/2.06)**, version 2.0.6
license
* **[Pillow](http://python-imaging.github.io/)**
#### Documentation
Kurt's documentation is hosted [on Read the Docs](http://kurt.readthedocs.org/).
#### License
Kurt is released under the [LGPL](http://www.gnu.org/licenses/lgpl) Version 3.