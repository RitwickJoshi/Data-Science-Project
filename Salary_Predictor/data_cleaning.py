# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 21:54:56 2020

@author: Ritwick Joshi
"""

import pandas as pd

df = pd.read_csv('data_scientist_jobs_glassdoor_500.csv')

#salary parser

#adding new column for "per hour" and "employer provided salary"
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

#removing the unknown salary as we are predicting salary which is the most important stuff
df = df[df['Salary Estimate']!= '-1']

#removing unwanetd signs etc
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
sign_remove = salary.apply(lambda x: x.replace('K',"").replace("$",''))
sign_remove_hr = sign_remove.apply(lambda x: x.lower().replace('per hour', "").replace('employer provided salary', "").replace(":",""))

#calcualting min max and avg
df['min_salary'] = sign_remove_hr.apply(lambda x:int(x.split('-')[0]))
df['max_salary'] = sign_remove_hr.apply(lambda x:int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2


#company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#state of company

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
#df.job_state.value_counts()

#age of company

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020-x)

#job desc parsing
#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#R studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)


#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.columns
df_wanted = df.drop(['Headquarters', 'Competitors'], axis = 1)

df_wanted.to_csv('salary_and_other_data_cleaned.csv', index = False)


pd.read_csv('salary_and_other_data_cleaned.csv')
