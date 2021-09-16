import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./salary_and_other_data_cleaned.csv')


df.head()


df.columns


def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst' 
    elif 'machine learning' in title.lower():
        return 'machine learning'
    elif 'director' in title.lower():
        return 'director'
    elif 'manager' in title.lower():
        return 'manager'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() \
        or 'principal' in title.lower() or 'sr.' in title.lower():
        return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'junior'
    else:
        return 'na'
    


# Job Title simplified
df['job_simp'] = df['Job Title'].apply(title_simplifier)
df.job_simp.value_counts()


# Job seniority
df['seniority'] = df['Job Title'].apply(seniority)
df.seniority.value_counts()


# Fixing Los Angeles- fixed
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() get_ipython().getoutput("='los angeles' else 'CA')")
df['job_state'].value_counts()



