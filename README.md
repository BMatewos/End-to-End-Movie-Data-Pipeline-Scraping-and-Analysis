## Objective
The goal of this project is to extract detailed and structured information about movies from IMDb — a widely trusted and comprehensive source of movie data. Specifically, we aim to gather data such as the movie title, genre, release year, and IMDb rating. Additionally, we will enrich this dataset by integrating it with a supplementary movie dataset from Kaggle, creating a comprehensive data source for further analysis.

This structured dataset will then be stored in a database, enabling easy access and manipulation. By organizing and structuring this data, we unlock its potential for applications such as building recommendation systems, conducting trend analyses, and creating visualizations to understand movie ratings and genre popularity over time.

The project will support answering questions such as:

Which genres have consistently high ratings over the years?
How have average movie ratings evolved over decades?
What are the key characteristics of top-rated movies?
This project will lay the foundation for these kinds of insights by efficiently collecting, organizing, and storing movie data from IMDb and Kaggle.

### Steps

#### Step 1: Defining Requirements
First, we will define our requirements by identifying the specific data fields to be extracted from IMDb and Kaggle. These fields may include:

Title: The name of the movie.
Release Year: The year the movie was released.
Genres: The movie's genres (e.g., drama, action, comedy).
IMDb Rating: The average rating given by users.
Runtime: The length of the movie.
Summary/Description: A brief synopsis of the movie.
We will also consider attributes from the Kaggle dataset that may include:

Additional movie metrics (e.g., box office revenue, director, actors, production companies, etc.).
Once we have a clear understanding of the data needed, we will decide on the format for storing the extracted information. Given the large dataset, we will choose a MySQL database to facilitate efficient querying and analysis.

#### Step 2: Setting Up the Web Scraper
We will set up a web scraper using appropriate libraries and tools:

BeautifulSoup will be used for parsing and navigating HTML content to scrape static pages.
The setup will include sending HTTP requests to IMDb pages and parsing the responses with CSS selectors or XPath expressions to locate and extract the required data fields. We will also implement error-handling mechanisms to manage issues like CAPTCHA and potential changes in the website structure.

#### Step 3: Data Flow
The data flow will be structured into three main stages:

Scraping Raw HTML: The scraper will send requests to IMDb pages and retrieve raw HTML content.
Parsing and Extracting Data: The raw HTML will be processed using libraries such as BeautifulSoup, Scrapy, or Selenium to extract relevant information.
Storing Structured Data: The extracted data will be stored in a MySQL database, where we will implement data validation to ensure data integrity and avoid missing or duplicate entries.
#### Step 4: Integrating the Kaggle Dataset
After the IMDb data is extracted, we will load the Kaggle dataset (using pandas or another data-handling tool). We will clean and align both datasets to ensure a consistent format and merge them based on a common attribute like the movie title or IMDb ID.

#### Step 5: Ethics and Legalities
Before starting, we will review IMDb’s Terms of Use and their robots.txt file to ensure compliance with their scraping policies. To avoid overwhelming IMDb’s servers, we will incorporate rate-limiting by adding delays between requests. This responsible approach will help prevent the scraper from being flagged or blocked.

#### Step 6: Testing
We will conduct thorough testing to ensure the scraper operates as expected. This involves running the scraper on a small subset of IMDb pages to verify the accuracy of the data extraction. During this phase, we will debug any issues in parsing logic and add error-handling mechanisms to handle failed requests, timeouts, and unexpected website changes. We will also test the scraper's ability to handle larger datasets efficiently.

#### Step 7: Data Cleaning and Storage
After gathering and merging the data, we will clean the dataset by:

Removing duplicates.
Filling in missing values.
Standardizing data formats.
The final, cleaned data will be stored in the MySQL database for easy access and further analysis.

#### Step 8: Analyzing and Visualizing Results
Once the data is stored in the database, we will conduct analysis using SQL queries to identify trends and insights. We will use visualization tools like Matplotlib or Seaborn to create charts and graphs that reveal patterns, such as:

Average ratings by genre over the years.
Trends in movie ratings over decades.
Key characteristics of top-rated movies.
These visualizations and analyses will provide valuable insights into the world of film and support applications like recommendation systems and trend analysis.

## Diving into the project
### Webscrapping

To begin, we sent HTTP requests to IMDb’s Top 1000 Movies pages using the requests library. Since IMDb typically paginates its lists, we looped through the pages in increments of 250, fetching data from each. To mimic a browser request and avoid being blocked, we added a custom user-agent header. The responses contained the HTML content of each page, which we processed in subsequent steps.

Next, we extracted the embedded JSON-LD data from the page’s HTML. JSON-LD is a structured format that includes metadata about the movies. Using regular expressions, we located the <script> tag containing this data and parsed it into a Python dictionary. This allowed us to access detailed movie information efficiently.

From the parsed JSON-LD data, we extracted key details for each movie, such as the title, description, URL, ratings, content rating, genre, and duration. For fields that were missing in the source data, we assigned default values like 'N/A'. This ensured a consistent structure for the dataset. The movie details were stored as individual records in a Python list, creating a comprehensive collection of information for the Top 1000 Movies.

Once all the data was gathered, we saved it in a JSON file named movies_data.json. This file retained the hierarchical structure of the data and could be used for further processing. To make the data more accessible for analysis and visualization, we converted the JSON file into a Pandas DataFrame and exported it to a CSV file named movies_data.csv.The data is now available in both JSON and CSV formats, enabling further exploration and analysis.

### Data Merging

This phase of the project focused on integrating and cleaning data by merging the IMDb Top 1000 Movies dataset with a larger dataset of over 1 million movies from Kaggle. After standardizing column names, the datasets were merged using the title column as the title, enriching the IMDb dataset with additional details like production information, cast, budget, and revenue. Unnecessary columns were dropped to streamline the data, and duplicate entries were removed based on movie titles. The duration column was converted into a standardized time format (HH:MM:SS), and rows with missing values were eliminated to ensure a clean and complete dataset. The resulting dataset is now enriched, standardized, and ready for further analysis or visualization, providing a comprehensive resource for exploring movie trends and metrics.

### Data Storage

In this stage of the project, we focused on populating a MySQL database with the cleaned movie data. The process began by establishing a connection to the database using pymysql, followed by the creation of multiple tables to store different types of information about movies. These tables include Movies, Genres, Movie_Genre, Cast, Movie_Cast, Directors, Movie_Director, Writers, Movie_Writer, and Movie_Production. The SQL CREATE TABLE commands ensured that each table had the necessary fields, relationships, and foreign key constraints to maintain data integrity.

Once the database structure was in place, we proceeded to insert the cleaned movie data into the appropriate tables. The insert_movies function populated the Movies table with basic movie details such as title, rating, release date, and budget. Other functions such as insert_genres, insert_cast, insert_directors, insert_writers, and insert_production handled the insertion of related data into their respective tables, creating mappings between movies and their genres, cast members, directors, writers, and production companies. These functions ensured that genres, cast, directors, writers, and production companies were inserted uniquely and that the relationships between movies and these entities were accurately recorded using join tables.

After executing the insertion queries for all relevant tables, the database was successfully populated with structured movie data. The relationships between different entities (e.g., movies and their genres, cast, directors) were maintained through foreign key references, ensuring data consistency across tables. The data is now ready for further analysis, querying, or visualization from the MySQL database.
