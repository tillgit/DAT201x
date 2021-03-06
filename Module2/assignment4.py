import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# need html5lib (conda install html5lib)
df = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')
df = df[0]

# TODO: Rename the columns so that they are similar to the
# column definitions provided to you on the website.
# Be careful and don't accidentially use any names twice.
#
df.columns = ['RK','PP_PLAYER','SH_TEAM','GP','G','A','PTS','+/-','PIM','PTS/G','SOG','PCT','GWG','PP_G','PP_A','SH_G','SH_A']
df.columns = df.columns.unique()
print(df.head())
# TODO: Get rid of any row that has at least 4 NANs in it,
# e.g. that do not contain player points statistics
#
df = df.dropna(thresh=13) # since len(df.columns) = 17 ( - 4 )

# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
print(df.describe())

# df = df.dropna()
df = df.drop_duplicates(keep='first') # safe drop
# remove first row (title)
df = df.drop(1)

# TODO: Get rid of the 'RK' column
#
df = df.drop('RK', axis=1)

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
df  = df.reset_index(drop=True)

# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
for s in df.columns[2:]:
    df[s] = pd.to_numeric(df[s], errors='coerce')

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
#
df = df.dropna().reset_index(drop=True)