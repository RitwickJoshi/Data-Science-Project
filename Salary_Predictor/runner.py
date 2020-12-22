# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:30:36 2020

@author: Ritwick Joshi
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/Data-Science-Project/chromedriver_win32/chromedriver.exe"

df = gs.get_jobs("data scientist", 15, False, path, 1000)


