# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:30:36 2020

@author: Ritwick Joshi
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/DESKTOP/Desktop/Compiler/Pythonfiles/Data-Science-Project/chromedriver_win32/chromedriver.exe"

profile="data scientist"
num_jobs = 500
verbose_program = False
internet_connection_time = 20

df = gs.get_jobs(profile, num_jobs, verbose_program, path, internet_connection_time)

df.to_csv('data_scientist_jobs_glassdoor_500.csv', index=False)

