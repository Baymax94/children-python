#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

# open image
image = Image.open('E://GitHub//children-python//人工智能初步（选修）//2.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim')
print(code)
