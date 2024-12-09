# %%
import json
import pandas as pd

# %%

with open('movies_data.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

csv_file_path = 'movies_data.csv'
df.to_csv(csv_file_path, index=False, encoding='utf-8')
#print(f"Data successfully saved to '{csv_file_path}'")




