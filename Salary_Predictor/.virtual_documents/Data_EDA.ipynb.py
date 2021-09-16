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


# Job Description Length
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))
df['desc_len']


# hourly wage into annual
df['min_salary'] = df.apply(lambda x: x.min_salary*2 if x.hourly == 1 else x.min_salary, axis = 1)
df['max_salary'] = df.apply(lambda x: x.max_salary*2 if x.hourly == 1 else x.max_salary, axis = 1)


df[['min_salary','max_salary']]


df.columns


df['company_txt'] = df.company_txt.apply(lambda x: x.replace('\n', ''))


df.describe()


df.columns


df.Rating.hist()


df.avg_salary.hist()


df.age.hist()


df.boxplot('avg_salary')


df.boxplot(['avg_salary', 'age'])


df.boxplot('Rating')


df_corr = df[['age', 'Rating', 'avg_salary', 'desc_len']]



df_corr.corr()


cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(df_corr.corr(), vmax=.3, center=0, cmap=cmap,
           square=True ,linewidths=.5, cbar_kws={'shrink': .5})


# df.columns
df_catergorical = df[['Location', 'Size', 'Type of ownership',
            'Industry', 'Sector', 'Revenue','Company Name', 
            'company_txt','job_state', 'python_yn', 'R_yn', 
            'spark', 'aws', 'excel', 'job_simp', 'seniority', 
            'avg_salary']]


for i in df_catergorical.columns:
    sns.barplot()
