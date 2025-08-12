import pandas as pd

# Load Men_data and clubsTable
# (Assume Men_data is already loaded in the notebook, so this is just for reference)
# Men_data = pd.read_csv('path_to_Men_data.csv')
clubs = pd.read_csv('../data/clubsTable.csv')

# Merge club name into Men_data on the club code/abbreviation
# Assume 'Club' in Men_data matches 'Club' or 'ClubCode' in clubsTable
# Let's check the columns in clubsTable
print(clubs.columns)

# Example merge (update the column names as needed):
# Men_data = Men_data.merge(clubs[['Club', 'ClubName']], on='Club', how='left')
# print(Men_data[['Club', 'ClubName']].head())

# If you want to run this in the notebook, use the following code:
# Men_data = Men_data.merge(clubs[['Club', 'ClubName']], on='Club', how='left')
# Men_data.head()
