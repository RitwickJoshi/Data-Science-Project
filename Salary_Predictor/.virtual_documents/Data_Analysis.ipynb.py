import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('salary_and_other_data_cleaned.csv')


df. head()


df.columns


def title_simplification(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'

def senior(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower() or 'sr.' in title.lower():
        return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'junior' in title.lower():
        return 'jr'
    else:
        return 'na'



df['job_simple'] = df['Job Title'].apply(title_simplification)


df['job_simple'].value_counts()


df['seniority'] = df['Job Title'].apply(senior)
df['seniority'].value_counts()


df['job_state'].value_counts()


df['desc_length'] = df['Job Description'].apply(lambda x: len(x))



df['desc_length']


#hourly wage calculation
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly == 1 else x.min_salary, axis = 1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly == 1 else x.max_salary, axis = 1)


df['min_salary'].value_counts()


df[df.hourly == 1][['hourly','min_salary', 'max_salary']]


df['company_txt'] = df['company_txt'].apply(lambda x: x.replace('\n',''))


df['company_txt']


df.describe()


df.columns


df.Rating.hist()


df.avg_salary.hist()


df.age.hist()


df.columns


df.desc_length.hist()


df.avg_salary.boxplot(['min_salary, max_salary'])


df.boxplot(['age','avg_salary','desc_length','Rating'])


df.boxplot(['age','avg_salary','Rating'])


df.boxplot(['Rating'])



