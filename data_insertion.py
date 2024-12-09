# %%
import pymysql

# %%

conn = pymysql.connect(
    host='mysql.clarksonmsda.org',
    port=3306,
    user='ia626',
    passwd='ia626clarkson',
    db='ia626',
    autocommit=True
)
cur = conn.cursor()

# Insert data into the Movies table
def insert_movies(dataframe):
    movies_query = """
    INSERT INTO berhemd_Movies (title, url, description, rating, ratingcount, image, contentrating, 
                        vote_average, release_date, original_language, popularity, 
                        budget, revenue, duration_time)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for _, row in dataframe.iterrows():
        cur.execute(movies_query, (
            row['title'], row['url'], row['description'], row['rating'], row['ratingcount'],
            row['image'], row['contentrating'], row['vote_average'], row['release_date'],
            row['original_language'], row['popularity'], row['budget'], row['revenue'], 
            row['duration_time']
        ))

# Insert data into the Genres table and create mappings
def insert_genres(dataframe):
    genres_query = "INSERT IGNORE INTO berhemd_Genres (genre_name) VALUES (%s)"
    movie_genre_query = "INSERT INTO berhemd_Movie_Genre (movie_id, genre_id) VALUES (%s, %s)"
    
    for _, row in dataframe.iterrows():
        if row['genres']:
            genres = row['genres'].split(', ')  # Assuming genres are comma-separated
            for genre in genres:
                # Insert genre into Genres table
                cur.execute(genres_query, (genre,))
                # Get genre_id
                cur.execute("SELECT genre_id FROM berhemd_Genres WHERE genre_name = %s", (genre,))
                genre_id = cur.fetchone()[0]
                # Map genre to movie
                cur.execute("SELECT movie_id FROM berhemd_Movies WHERE title = %s", (row['title'],))
                movie_id = cur.fetchone()[0]
                cur.execute(movie_genre_query, (movie_id, genre_id))

# Insert data into the Cast table and create mappings
def insert_cast(dataframe):
    cast_query = "INSERT IGNORE INTO berhemd_Cast (cast_name) VALUES (%s)"
    movie_cast_query = "INSERT INTO berhemd_Movie_Cast (movie_id, cast_id) VALUES (%s, %s)"
    
    for _, row in dataframe.iterrows():
        if row['cast']:
            cast_members = row['cast'].split(', ')  # Assuming cast members are comma-separated
            for cast_member in cast_members:
                # Insert cast member into Cast table
                cur.execute(cast_query, (cast_member,))
                # Get cast_id
                cur.execute("SELECT cast_id FROM berhemd_Cast WHERE cast_name = %s", (cast_member,))
                cast_id = cur.fetchone()[0]
                # Map cast member to movie
                cur.execute("SELECT movie_id FROM berhemd_Movies WHERE title = %s", (row['title'],))
                movie_id = cur.fetchone()[0]
                cur.execute(movie_cast_query, (movie_id, cast_id))

# Insert data into the Directors table and create mappings
def insert_directors(dataframe):
    directors_query = "INSERT IGNORE INTO berhemd_Directors (director_name) VALUES (%s)"
    movie_director_query = "INSERT INTO berhemd_Movie_Director (movie_id, director_id) VALUES (%s, %s)"
    
    for _, row in dataframe.iterrows():
        if row['director']:
            directors = row['director'].split(', ')  # Assuming directors are comma-separated
            for director in directors:
                # Insert director into Directors table
                cur.execute(directors_query, (director,))
                # Get director_id
                cur.execute("SELECT director_id FROM berhemd_Directors WHERE director_name = %s", (director,))
                director_id = cur.fetchone()[0]
                # Map director to movie
                cur.execute("SELECT movie_id FROM berhemd_Movies WHERE title = %s", (row['title'],))
                movie_id = cur.fetchone()[0]
                cur.execute(movie_director_query, (movie_id, director_id))

# Insert data into the Writers table and create mappings
def insert_writers(dataframe):
    writers_query = "INSERT IGNORE INTO berhemd_Writers (writer_name) VALUES (%s)"
    movie_writer_query = "INSERT INTO berhemd_Movie_Writer (movie_id, writer_id) VALUES (%s, %s)"
    
    for _, row in dataframe.iterrows():
        if row['writers']:
            writers = row['writers'].split(', ')  # Assuming writers are comma-separated
            for writer in writers:
                # Insert writer into Writers table
                cur.execute(writers_query, (writer,))
                # Get writer_id
                cur.execute("SELECT writer_id FROM berhemd_Writers WHERE writer_name = %s", (writer,))
                writer_id = cur.fetchone()[0]
                # Map writer to movie
                cur.execute("SELECT movie_id FROM berhemd_Movies WHERE title = %s", (row['title'],))
                movie_id = cur.fetchone()[0]
                cur.execute(movie_writer_query, (movie_id, writer_id))

# Insert data into the Movie_Production table
def insert_production(dataframe):
    production_query = """
    INSERT INTO berhemd_Movie_Production (movie_id, production_company, production_country) 
    VALUES (%s, %s, %s)
    """
    for _, row in dataframe.iterrows():
        if row['production_companies'] or row['production_countries']:
            production_companies = row['production_companies'].split(', ')
            production_countries = row['production_countries'].split(', ')
            for company, country in zip(production_companies, production_countries):
                cur.execute("SELECT movie_id FROM berhemd_Movies WHERE title = %s", (row['title'],))
                movie_id = cur.fetchone()[0]
                cur.execute(production_query, (movie_id, company, country))

# Populate all tables
try:
    insert_movies(df_merged_cleaned)
    insert_genres(df_merged_cleaned)
    insert_cast(df_merged_cleaned)
    insert_directors(df_merged_cleaned)
    insert_writers(df_merged_cleaned)
    insert_production(df_merged_cleaned)
    print("Data populated successfully.")
except Exception as e:
    print(f"Error populating data: {e}")
finally:
    cur.close()
    conn.close()



