# %%
import pandas as pd

# %%
movies_1million1 = pd.read_csv('TMDB_all_movies.csv')  
movies_1000 = pd.read_csv('movies_data.csv')

movies_1million1.columns = movies_1million1.columns.str.lower()
movies_1000.columns = movies_1000.columns.str.lower()


if 'title' in movies_1000.columns and 'title' in movies_1million1.columns:
    merged_data = pd.merge(
        movies_1000,
        movies_1million1,
        on='title',
        how='left',
        suffixes=('_1000', '_1million')  
    )

    
    merged_data = merged_data.loc[:, ~merged_data.columns.duplicated()]

    
    print(f"Number of rows after merging: {merged_data.shape[0]}")
    print(f"Number of unique titles after merging: {merged_data['title'].nunique()}")
else:
    print("The 'title' column is missing in one of the DataFrames.")

# Display the resulting merged DataFrame
merged_data.head()



