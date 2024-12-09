# %%


# %%
columns_to_keep = [
    'title', 'url', 'description', 'rating',
    'ratingcount', 'image', 'contentrating', 'genre', 'duration', 
    'vote_average', 'release_date', 
    'imdb_votes', 'original_language', 
    'popularity', 'genres', 'cast', 'director', 'writers', 
    'production_companies', 'production_countries', 'budget','revenue'
    
]
df_merged_filtered = merged_data[columns_to_keep]
#print(df_merged_filtered)

# %%
#drop duplicated rows based on movies title
df_merged =  df_merged_filtered.drop_duplicates(subset=['title'])
df_merged.reset_index(drop=True, inplace=True)


# %%
if 'duration' not in df_merged.columns:
    if 'actual_duration_column' in df_merged.columns:  
        df_merged.rename(columns={'actual_duration_column': 'duration'}, inplace=True)
    else:
        raise KeyError("The 'duration' column or 'actual_duration_column' is missing from the DataFrame.")

def convert_duration_to_time(duration):
    if not isinstance(duration, str) or pd.isna(duration):
        return None  
    
    duration = duration.replace("PT", "")
    hours = 0
    minutes = 0
    if "H" in duration:
        hours, duration = duration.split("H")
        hours = int(hours)
    if "M" in duration:
        minutes = int(duration.replace("M", ""))
    return f"{hours}:{minutes:02d}:00"

df_merged.loc[:, 'duration_time'] = df_merged['duration'].apply(convert_duration_to_time)

#print(df_merged.head())


# %%
df_merged_cleaned = df_merged.dropna()
df_merged_cleaned.reset_index(drop=True, inplace=True)

# Display the shape of the new DataFrame
# print(f"Original DataFrame shape: {df_merged.shape}")
# print(f"DataFrame shape after dropping null values: {df_merged_cleaned.shape}")

# %%
# drop duration
columns_to_drop = ['duration']
existing_columns_to_drop = [col for col in columns_to_drop if col in df_merged_cleaned.columns]

if existing_columns_to_drop:
    
    df_merged_cleaned = df_merged_cleaned.drop(columns=existing_columns_to_drop)
    print(f"Dropped columns: {existing_columns_to_drop}")
else:
    print(f"No columns to drop from the specified list: {columns_to_drop}")

df_merged_cleaned = df_merged_cleaned.reset_index(drop=True)



