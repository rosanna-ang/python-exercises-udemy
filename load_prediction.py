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

df = df['ApplicantIncome'].hist(bins=50)


plt.title('Applicant Income')
plt.savefig('mytable.png')


#table(ax, df)
#plt.savefig('mytable.png')
