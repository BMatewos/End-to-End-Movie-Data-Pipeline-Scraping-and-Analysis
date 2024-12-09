# %%
import requests
import re
import json


# %%
#url
base_url = "https://www.imdb.com/list/ls048276758/"
headers = {"User-Agent": "Mozilla/5.0"}

# %%

all_movies = []

for start in range(1, 1001, 250):
    url = f"{base_url}?start={start}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        json_ld_data = re.search(r'<script type="application/ld\+json">(.*?)</script>', response.text, re.DOTALL)
        
        if json_ld_data:
            movies_data = json.loads(json_ld_data.group(1))
            
            if "itemListElement" in movies_data:
                movies = movies_data["itemListElement"]
                
                for movie in movies:
                    movie_item = movie['item']
                    
                    movie_data = {
                        "Title": movie_item.get('name', 'N/A'),
                        "URL": movie_item.get('url', 'N/A'),
                        "Description": movie_item.get('description', 'N/A'),
                        "Rating": movie_item.get('aggregateRating', {}).get('ratingValue', 'N/A'),
                        "BestRating": movie_item.get('aggregateRating', {}).get('bestRating', 'N/A'),
                        "WorstRating": movie_item.get('aggregateRating', {}).get('worstRating', 'N/A'),
                        "RatingCount": movie_item.get('aggregateRating', {}).get('ratingCount', 'N/A'),
                        "Image": movie_item.get('image', 'N/A'),
                        "ContentRating": movie_item.get('contentRating', 'N/A'),
                        "Genre": movie_item.get('genre', 'N/A'),
                        "Duration": movie_item.get('duration', 'N/A')
                    }
                    
                    all_movies.append(movie_data)
        else:
            print("No JSON-LD data found on the page.")
    else:
        print(f"Failed to retrieve page starting at {start}. Status code: {response.status_code}")

with open("movies_data.json", "w") as json_file:
    json.dump(all_movies, json_file, indent=4)

print(f"Data for {len(all_movies)} movies successfully saved to 'movies_data.json'")



