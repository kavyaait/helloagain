#import libraries
import pandas as pd
import numpy as np

df2 = pd.read_csv(r'C:\Users\kavya\Documents\dataanalysis.csv')
#print(df)
#df2= df.copy()

# Making a list of missing value types
missing_values = ["n/a", "na", "?","Refused","Don\'t know/Not Sure","Don\'t know/not Sure","Not asked or Missing"]
df2 = pd.read_csv(r'C:\Users\kavya\Documents\dataanalysis.csv', na_values = missing_values)
#print(df2.isnull().sum())

cols_to_clean = ['GENHLTH','PHYSHLTH','MENTHLTH','SEX','AGE','EDUCA','EMPLOY1','CHILDREN','INCOME2','RENTHOM1','EXER']

#categorical conversion of education
df2['EDUCA'] = df2['EDUCA'].astype(str)
df2['EDUCA'] = df2['EDUCA'].map(lambda x: x.replace('College 1 year to 3 years (Some college or technical school)','Some college or technical school'))
df2['EDUCA'] = df2['EDUCA'].map(lambda x: x.replace('College 4 years or more (College graduate)','College graduate'))
df2['EDUCA'] = df2['EDUCA'].map(lambda x: x.replace('Grade 12 or GED (High school graduate)','High school graduate'))
df2['EDUCA'] = df2['EDUCA'].map(lambda x: x.replace('Grades 1 through 8 (Elementary)','Elementary'))
df2['EDUCA'] = df2['EDUCA'].map(lambda x: x.replace('Grades 9 through 11 (Some high school)','Some high school'))


#categorical conversion of income
df2['INCOME2'] = df2['INCOME2'].astype(str)
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $15,000 ($10,000 to less than $15,000)','Less than 15'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $20,000 ($15,000 to less than $20,000)','Less than 20'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $25,000 ($20,000 to less than $25,000)','Less than 25'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $35,000 ($25,000 to less than $35,000)','Less than 35'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $50,000 ($35,000 to less than $50,000)','Less than 50'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $75,000 ($50,000 to less than $75,000)','Less than 75'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('Less than $10,000','Less than 10'))
df2['INCOME2'] = df2['INCOME2'].map(lambda x: x.replace('$75,000 or more','More than 75'))

#categorical conversion of age
df2['AGE'] = df2['AGE'].astype(str)	
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 18 - 24','18-24'))
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 25 - 34','25-34'))
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 35 - 44','35-44'))
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 45 - 54','44-54'))
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 55 - 64','55-64'))
df2['AGE'] = df2['AGE'].map(lambda x: x.replace('Age 65 or older','65+'))


for col in cols_to_clean:	
	df2[col] = df2[col].astype(str)	
        #df2[col] = df2[col].map(lambda x: x.replace('Refused','NaN'))
	df2[col] = df2[col].map(lambda x: x.replace('Don\'t know/Not sure','NaN'))
	df2[col] = df2[col].map(lambda x: x.replace('Don\'t know/Not Sure','NaN'))
	df2[col] = df2[col].map(lambda x: x.replace('Not asked or Missing','NaN'))	
	df2[col] = df2[col].map(lambda x: x.replace(' ','_'))
        #df2[col] = df2[col].map(lambda x: x.replace('Refused','NaN'))
	df2[col] = df2[col].replace(r'^\s+$', 'NaN', regex=True)
        #df2[col] = df2[col].replace(?, np.nan)
	df2[col] = df2[col].replace(' ', '?')
	
        


#categorical conversion of general health
#df2['GENHLTH'] = df2['GENHLTH'].map(lambda x: x.replace('Poor','0'))
#df2['GENHLTH'] = df2['GENHLTH'].map(lambda x: x.replace('Fair','1'))
#df2['GENHLTH'] = df2['GENHLTH'].map(lambda x: x.replace('Good','2'))
#df2['GENHLTH'] = df2['GENHLTH'].map(lambda x: x.replace('Very good','3'))
#df2['GENHLTH'] = df2['GENHLTH'].map(lambda x: x.replace('Excellent','4'))



print(df2)

df2.to_csv(r'C:\Users\kavya\Documents\processedfiles\analysis1_weka9.csv', index=False)
