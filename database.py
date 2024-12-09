# %%
import pymysql

# %%


# Connect to the database
conn = pymysql.connect(
    host='mysql.clarksonmsda.org',
    port=3306,
    user='ia626',
    passwd='ia626clarkson',
    db='ia626',
    autocommit=True
)
cur = conn.cursor()


# %%

# SQL commands to create tables
create_movies_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    url TEXT,
    description TEXT,
    rating FLOAT,
    ratingcount INT,
    image TEXT,
    contentrating VARCHAR(50),
    vote_average FLOAT,
    release_date DATE,
    original_language VARCHAR(50),
    popularity FLOAT,
    budget BIGINT,
    revenue BIGINT,
    duration_time VARCHAR(50)
);
"""

create_genres_table = """
CREATE TABLE IF NOT EXISTS berhemd_Genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) UNIQUE NOT NULL
);
"""

create_movie_genre_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movie_Genre (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    genre_id INT,
    FOREIGN KEY (movie_id) REFERENCES berhemd_Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES  berhemd_Genres(genre_id) ON DELETE CASCADE
);
"""

create_cast_table = """
CREATE TABLE IF NOT EXISTS berhemd_Cast (
    cast_id INT AUTO_INCREMENT PRIMARY KEY,
    cast_name VARCHAR(255) UNIQUE NOT NULL
);
"""

create_movie_cast_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movie_Cast (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    cast_id INT,
    FOREIGN KEY (movie_id) REFERENCES berhemd_Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (cast_id) REFERENCES berhemd_Cast(cast_id) ON DELETE CASCADE
);
"""

create_directors_table = """
CREATE TABLE IF NOT EXISTS berhemd_Directors (
    director_id INT AUTO_INCREMENT PRIMARY KEY,
    director_name VARCHAR(255) UNIQUE NOT NULL
);
"""

create_movie_director_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movie_Director (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    director_id INT,
    FOREIGN KEY (movie_id) REFERENCES berhemd_Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (director_id) REFERENCES berhemd_Directors(director_id) ON DELETE CASCADE
);
"""

create_writers_table = """
CREATE TABLE IF NOT EXISTS berhemd_Writers (
    writer_id INT AUTO_INCREMENT PRIMARY KEY,
    writer_name VARCHAR(255) UNIQUE NOT NULL
);
"""

create_movie_writer_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movie_Writer (
    mapping_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    writer_id INT,
    FOREIGN KEY (movie_id) REFERENCES berhemd_Movies(movie_id) ON DELETE CASCADE,
    FOREIGN KEY (writer_id) REFERENCES berhemd_Writers(writer_id) ON DELETE CASCADE
);
"""

create_movie_production_table = """
CREATE TABLE IF NOT EXISTS berhemd_Movie_Production (
    production_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    production_company VARCHAR(255),
    production_country VARCHAR(100),
    FOREIGN KEY (movie_id) REFERENCES berhemd_Movies(movie_id) ON DELETE CASCADE
);
"""

# Execute the SQL commands
table_commands = [
    create_movies_table,
    create_genres_table,
    create_movie_genre_table,
    create_cast_table,
    create_movie_cast_table,
    create_directors_table,
    create_movie_director_table,
    create_writers_table,
    create_movie_writer_table,
    create_movie_production_table
]

for command in table_commands:
    try:
        cur.execute(command)
        print(f"Table created successfully:\n{command.split('(')[0].strip()}")
    except Exception as e:
        print(f"Error creating table: {e}")


cur.close()
conn.close()



