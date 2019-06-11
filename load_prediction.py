import pandas as pd
import numpy as np
import matplotlib as plt

import matplotlib.pyplot as plt


from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

df = pd.read_csv("train.csv") #Reading the dataset in a dataframe using Pandas

print(df.describe())
print(df["Property_Area"].value_counts())

df1 = df['ApplicantIncome'].hist(bins=50)
plt.title('Applicant Income')
plt.savefig('ApplicantIncome.png')

df['Credit_History'].hist(bins=50)
plt.title('Credit History')
plt.savefig('CreditHistory.png')

plt.savefig('fname.png', dpi=None, facecolor='b', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)


plot = df.plot(x='ApplicantIncome',y='LoanAmount')
plot2 = df.plot(x='ApplicantIncome',y='CoapplicantIncome')
fig = plot.get_figure()
fig.savefig("output1.png")
fig = plot2.get_figure()
fig.savefig("output2.png")

"""
df.plot(x='ApplicantIncome',y='LoanAmount')
plt.title('Third One')
plt.savefig('test.png')
"""

boxplot1 = df.boxplot(column='ApplicantIncome')
plt.title('boxplot1')
plt.savefig('boxplot1.png')
print ('==============================')
print ('boxplot1:')
print (boxplot1)
print ('==============================')
print ('')
print ('')
print ('')

boxplot2 = df.boxplot(column='ApplicantIncome', by = 'Education')
plt.title('boxplot2')
plt.savefig('boxplot2.png')
print ('==============================')
print ('boxplot2:')
print (boxplot2)
print ('==============================')
print ('')
print ('')
print ('')




temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())
print ('==============================')
print ('Frequency Table for Credit History:')
print (temp1)
print ('==============================')
print ('')
print ('')
print ('')
print ('==============================')
print ('Probility of getting loan for each Credit History class:')
print (temp2)
print ('==============================')
print ('')
print ('')
print ('')
