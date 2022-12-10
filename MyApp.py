#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:22:11 2022

@author: stoutjd
"""

from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
from PyQt6 import uic


import sys

app = QApplication(sys.argv)

# window = MainWindow()
window = uic.loadUi('test.ui')
window.show()


app.exec()
