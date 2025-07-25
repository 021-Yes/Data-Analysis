import pandas as pd

# Uploading dataframe 
df = pd.read_csv('GoogleApps.csv')


# What is the name of the first application containing in the dataset?
print(df.head(1))
# >Photo Editor & Candy Camera & Grid & ScrapBook

# What is the category of the last application containing in the dataset?
print(df.tail(1))
# >LIFESTYLE

# How many columns are there in the dataset?
print(df.info())
# >total 12 columns

# What is the type of data stored in each column?
#  0   App             7352 non-null   object
#  1   Category        7352 non-null   object
#  2   Rating          7352 non-null   float64
#  3   Reviews         7352 non-null   int64
#  4   Size            7352 non-null   float64
#  5   Installs        7352 non-null   float64
#  6   Type            7352 non-null   object
#  7   Price           7352 non-null   float64
#  8   Content Rating  7352 non-null   object
#  9   Last Updated    7352 non-null   object
#  10  Current Ver     7352 non-null   object
#  11  Android Ver     7352 non-null   object

# Specify the arithmetic mean and median for the size of the applications.
print(df.describe())
# mean size: 22.769578
# median size: 14.000000

# How much does the most expensive application cost?
#4 00.000000

# *Specify the arithmetic mean and median for the number of application installs.
# 8.662313e+06
# 1.000000e+05
