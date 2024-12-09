# # Movie Data Scraping and Analysis
## Objective
The goal of this project is to extract detailed and structured information about movies from IMDb — a widely trusted and comprehensive source of movie data. Specifically, we aim to gather data such as the movie title, genre, release year, and IMDb rating. Additionally, we will enrich this dataset by integrating it with a supplementary movie dataset from Kaggle, creating a comprehensive data source for further analysis.

This structured dataset will then be stored in a database, enabling easy access and manipulation. By organizing and structuring this data, we unlock its potential for applications such as building recommendation systems, conducting trend analyses, and creating visualizations to understand movie ratings and genre popularity over time.

## Initial Question
"How can we store and analyze movie ratings over time, and are there any correlations between movie genres and their ratings?"

## Methodology
**Data Extraction**:

To begin, we initiated HTTP requests to IMDb’s Top 1000 Movies pages using the `requests` library. Since IMDb paginates its lists, we looped through the pages in increments of 250, fetching data from each page. To mimic a browser request and avoid being blocked, we included a custom user-agent header in the requests. The responses returned the HTML content of each page, which we processed in the subsequent steps.

 ### Data Extraction Process

1. **Scraping Data from IMDb**:
    - We used the `BeautifulSoup` library to scrape movie details from IMDb.
    - The raw data was initially stored in **JSON format** for structured access.

2. **Extracting Embedded JSON-LD Data**:
    - JSON-LD is a structured data format embedded in the HTML of IMDb pages, containing rich metadata about the movies.
    - We utilized regular expressions to locate the `<script>` tag containing this JSON-LD data and parsed it into a Python dictionary.
    - This method allowed us to efficiently access detailed movie information.

3. **Extracting Key Movie Details**:
    - From the parsed JSON-LD data, we extracted the following key details for each movie:
        - Title
        - Description
        - URL
        - IMDb Rating
        - Content Rating
        - Genre
        - Duration
    - For any missing fields in the source data, we assigned default values like ‘N/A’ to maintain a consistent structure across all records.

4. **Storing Data**:
    - Each movie's details were stored as individual records in a Python list, forming a comprehensive collection of information for the Top 1000 Movies.
    - Once all the data was gathered, we saved it into a **JSON file** named `movies_data.json`. This file retained the hierarchical structure of the data, which made it suitable for further processing.
    
5. **Data Conversion for Analysis**:
    - For easier analysis and visualization, we converted the JSON data into a Pandas DataFrame and exported it as a **CSV file** named `movies_data.csv`.
    - This provided us with both **JSON** and **CSV** formats for further exploration and analysis.


### Data Intergration and Cleaning

This phase of the project focused on integrating and cleaning data by merging the IMDb Top 1000 Movies dataset with a larger dataset of over 1 million movies from Kaggle. The integration process was carried out in the following steps:
link for kaggle dataset:

1. **Standardizing Column Names**:
    - Both datasets were reviewed, and column names were standardized to ensure consistency across the two datasets.

2. **Merging Datasets**:
    - The datasets were merged using the `title` column as the common key. This enriched the IMDb dataset with additional movie details from the Kaggle dataset, such as:
        - Production information
        - Cast
        - Budget
        - Revenue

3. **Data Cleaning**:
    - Removed duplicates and handled missing values to ensure data consistency.
    - Unnecessary columns were dropped to streamline the dataset.
    - Duplicate entries were removed based on movie titles to ensure uniqueness.
    - The `duration` column was converted into a standardized time format (HH:MM:SS).
    - Rows with missing values were eliminated to ensure a clean and complete dataset.

The resulting dataset is now enriched, standardized, and ready for further analysis or visualization, providing a comprehensive resource for exploring movie trends and metrics.


### Data Storage

In this stage of the project, we focused on populating a MySQL database with the cleaned movie data. The process began by establishing a connection to the database using pymysql, followed by the creation of multiple tables to store different types of information about movies. These tables include Movies, Genres, Movie_Genre, Cast, Movie_Cast, Directors, Movie_Director, Writers, Movie_Writer, and Movie_Production. The SQL CREATE TABLE commands ensured that each table had the necessary fields, relationships, and foreign key constraints to maintain data integrity.

Once the database structure was in place, we proceeded to insert the cleaned movie data into the appropriate tables. The insert_movies function populated the Movies table with basic movie details such as title, rating, release date, and budget. Other functions such as insert_genres, insert_cast, insert_directors, insert_writers, and insert_production handled the insertion of related data into their respective tables, creating mappings between movies and their genres, cast members, directors, writers, and production companies. These functions ensured that genres, cast, directors, writers, and production companies were inserted uniquely and that the relationships between movies and these entities were accurately recorded using join tables.

After executing the insertion queries for all relevant tables, the database was successfully populated with structured movie data. The relationships between different entities (e.g., movies and their genres, cast, directors) were maintained through foreign key references, ensuring data consistency across tables. The data is now ready for further analysis, querying, or visualization from the MySQL database.

### Testing the database
#### testing the relationships between tables
Check if the relationships between tables are working by performing some JOIN queries. For example, to check which movies belong to a particular genre, you can perform a join between Movies and Movie_Genre:

<img width="209" alt="sql query" src="https://github.com/user-attachments/assets/bf3a1627-a639-4264-90ff-37f26bbfc56c">

- Result

  <img width="157" alt="result 1" src="https://github.com/user-attachments/assets/53f1fd63-762c-4247-8385-0c57e0b99dc1">

  #### Check for Missing or Null Values
  Ensure that there are no missing or null values in the important fields (like movie_id, genre_name, cast_name, etc.).
  - Query
  
  <img width="238" alt="query 2" src="https://github.com/user-attachments/assets/c48d705e-6523-46aa-b547-a554ab963a62">


  - Result
  
  <img width="570" alt="result" src="https://github.com/user-attachments/assets/47a63c7c-f74a-464d-8c62-1eb005984290">

  The result returned show that there is no missing or null values fro the dataset in the database



