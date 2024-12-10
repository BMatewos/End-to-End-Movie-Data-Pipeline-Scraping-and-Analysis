# Movie Data Scraping and Analysis

# Table of Contents

- [Objective](#objective)
- [Data Sources](#data-sources)
- [Initial Question](#initial-question)
- [Technologies Used](#technologies-used)
- [Methodology](#methodology)
  - [Data Extraction](#data-extraction)
  - [Data Extraction Process](#data-extraction-process)
    - [Scraping Data from IMDb](#scraping-data-from-imdb)
    - [Extracting Embedded JSON-LD Data](#extracting-embedded-json-ld-data)
    - [Extracting Key Movie Details](#extracting-key-movie-details)
    - [Storing Data](#storing-data)
    - [Data Conversion for Analysis](#data-conversion-for-analysis)
  - [Data Integration and Cleaning](#data-integration-and-cleaning)
  - [Database Setup](#database-setup)
  - [Data Insertion](#data-insertion)
- [Analysis Results](#Analysis-Results)
- [Results and Discussions](#Results-and-Discussions)
- [Code API Appendix](#Code-API-Appendix)
- [Licensing and Credits](#Licensing-and-Credits)
- [How to Run the Project](#how-to-run-the-project)




## Objective
The goal of this project is to extract detailed and structured information about movies from IMDb — a widely trusted and comprehensive source of movie data. Specifically, we aim to gather data such as the movie title, genre, release year, and IMDb rating. Additionally, we will enrich this dataset by integrating it with a supplementary movie dataset from Kaggle, creating a comprehensive data source for further analysis.

This structured dataset will then be stored in a database, enabling easy access and manipulation. By organizing and structuring this data, we unlock its potential for applications such as building recommendation systems, conducting trend analyses, and creating visualizations to understand movie ratings and genre popularity over time.

## Data Sources

1. **IMDb Top 1000 Movies**: A list of the top 1000 movies, including key attributes such as title, genre, release year, IMDb rating, and runtime.
2. **Kaggle Movie Dataset**: A larger dataset of over 1 million movies, containing additional information such as director, cast, production details, and box office revenue.

link:https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates


These two datasets were merged on the movie title to create an enriched database containing both basic and advanced movie details.

## Initial Question
"How can we store and analyze movie ratings in a database, and are there any correlations between movie genres and their ratings?"

## Technologies Used

- **Python**: For web scraping, data cleaning, and processing.
- **BeautifulSoup**: For scraping and parsing HTML data from IMDb.
- **Pandas**: For data cleaning, manipulation, and CSV conversion.
- **MySQL**: For storing and managing the structured movie data.
- **requests**: To send HTTP requests and retrieve IMDb pages.
- **Matplotlib/Seaborn**: For data visualization (future steps).
  

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

### Database Setup:
In this stage of the project, we focused on setting up a MySQL database to store the structured movie data. The first step was to establish a connection to the MySQL database using the `pymysql` library. With the connection in place, we proceeded to create multiple tables to store different types of movie-related information. These tables included:

- **Movies**: Stores basic movie details like title, rating, release date, and budget.
- **Genres**: Stores movie genres such as action, comedy, drama, etc.
- **Movie_Genre**: A join table to associate movies with their respective genres.
- **Cast**: Stores information about actors and actresses.
- **Movie_Cast**: A join table to link movies to their cast members.
- **Directors**: Stores director information.
- **Movie_Director**: A join table to link movies with their directors.
- **Writers**: Stores information about the writers of the movie.
- **Movie_Writer**: A join table to link movies with their writers.
- **Movie_Production**: Stores production company information.

Each table was created using SQL `CREATE TABLE` commands, ensuring the necessary fields, relationships, and foreign key constraints were included. These constraints were put in place to maintain data integrity across the different tables.

**Advantages of Database Setup**:
- **Data Integrity**: The use of foreign key constraints between tables ensures that data is consistent and accurate, preventing orphan records and ensuring relationships between entities (e.g., movies and genres, cast members, directors) are properly maintained.
- **Scalability**: By structuring the data in a relational database, it becomes easier to scale the project. New data or entities can be added without disrupting the existing data structure, making it a flexible solution for future data growth.
- **Efficient Querying**: Storing movie data in a structured database allows for complex querying and retrieval of specific information (e.g., fetching movies by genre, rating, or director). This enables efficient data analysis and supports further exploration of movie trends.
- **Data Centralization**: By storing all the data in a central database, it is easier to manage and maintain. All data related to movies, genres, cast, etc., is housed in one location, making it easier to access and update.

### Data Insertion:
Once the database structure was established, we moved on to inserting the cleaned movie data into the relevant tables. The insertion process involved using several functions to populate each table:

- **insert_movies**: This function inserted basic movie details, such as the movie title, IMDb rating, release date, and budget, into the `Movies` table.
- **insert_genres**: This function inserted movie genres into the `Genres` table.
- **insert_cast**: This function inserted cast members into the `Cast` table.
- **insert_directors**: This function inserted director information into the `Directors` table.
- **insert_writers**: This function inserted writer information into the `Writers` table.
- **insert_production**: This function inserted production company details into the `Movie_Production` table.

Additionally, the **join tables** (such as `Movie_Genre`, `Movie_Cast`, `Movie_Director`, `Movie_Writer`) were used to create relationships between the movies and their respective genres, cast members, directors, writers, and production companies. These functions ensured that each genre, cast, director, writer, and production company was inserted uniquely, maintaining the integrity of the data.

**Advantages of Data Insertion**:
- **Data Accuracy**: Using structured functions to insert data into specific tables ensures that each type of data (e.g., genres, cast, directors) is inserted correctly and avoids redundancy or errors.
- **Relationships Maintenance**: By using join tables to link movies with their respective genres, cast, and production teams, the relationships between these entities are accurately recorded and can be efficiently queried or updated.
- **Data Normalization**: The insertion process ensures that data is normalized, meaning that movie details are stored separately from other related data (such as cast or genre). This reduces duplication and makes it easier to update or modify data without affecting other tables.
- **Efficient Data Management**: With the database fully populated, it becomes easy to manage and update movie data. This structured approach makes future modifications, such as adding new movies or updating cast and production details, quick and straightforward.

After executing the insertion queries, the MySQL database was successfully populated with structured movie data. The relationships between entities (e.g., movies and their genres, cast members, directors) were maintained through foreign key references. This ensures that the data remains consistent and can be easily queried for further analysis, visualization, or reporting.

### Analysis Results

The analysis conducted on the enriched movie dataset produced the following insights:

### 1.Comparison of Average Revenue and Ratings Across Top Genres
- **Insight**:
- Some genres are both financially successful and highly rated, such as **Drama, Action, Crime, Thriller**, which excels in both revenue and rating.

- Other genres may generate high revenue but are less critically acclaimed (e.g., **Family, Adventure, Animation, Comedy, Fantasy** has high revenue but a relatively lower rating of 7.6).

- Conversely, some genres have higher ratings but lower revenue, like **Thriller, Crime**.

-  **Visualization**:
  <img width="674" alt="graph1" src="https://github.com/user-attachments/assets/99fa3f31-e86a-44bb-8038-a524931bb6ce">

### 2. Correlation Heatmap: Metrics Driving Movie Success
- **Insight**:
- Budget and revenue have the strongest correlation, emphasizing the role of financial investment in box office success.

- Popularity metrics (rating count and IMDb votes) strongly correlate with each other and moderately correlate with revenue, indicating their importance in a movie’s success

- High ratings alone do not guarantee financial success, as shown by the weak correlation between ratings and revenue.

- **Visualization**:
<img width="641" alt="correlation matrix" src="https://github.com/user-attachments/assets/68af1b02-9b78-4707-af8f-63b09fa63b2e">

### 3.Movie Poduction over years
- **Insight**:
- Spikes in Production: Peaks occur in the late 1930s, early 1960s, and early 2000s, likely tied to industry or cultural shifts.

- Fluctuations: Movie production varies greatly, with notable declines in some years, such as the late 1980s and 1990s.

- Industry Resilience: Despite fluctuations, the industry has sustained production over a century, adapting to challenges and changes.

- **Visualization**:
<img width="575" alt="movie production over years" src="https://github.com/user-attachments/assets/27c8f91c-a841-4660-a417-941c9df8cf38">


### Results and Discussions
#### Challenges and Limitations
During the project, several challenges arose, particularly in data cleaning and integration. The IMDb dataset and the external source had inconsistencies, missing values, and format mismatches, requiring extensive preprocessing to ensure that the data was reliable for analysis. This cleaning process, along with the merging of the two datasets, resulted in a reduction in the overall dataset size due to records with missing or incompatible information. Consequently, the scope of the analysis was limited by these data quality issues.

Another challenge was the limitations associated with scraping data from IMDb. Changes in the website structure, rate-limiting, and legal considerations made it difficult to collect consistent and complete data. These factors contributed to missing or incomplete records, further reducing the size and accuracy of the dataset. Despite these challenges, the project provided valuable insights, though the limitations in data quality and scraping techniques influenced the depth of the analysis.

#### Conclusion and Future Work
This project successfully integrated IMDb movie data with external datasets, storing the results in a structured database for efficient querying and analysis. The analysis revealed significant correlations between movie success factors like genre, budget, and popularity, and provided insights into trends over time.

In the future, we plan to extend the analysis to include additional factors such as marketing efforts, cast popularity, and director influence, as well as explore more advanced machine learning techniques to predict the success of movies based on these factors.

# Code API Appendix

In this section, we provide a detailed overview of the code and APIs used during the project. The main components include web scraping using the `BeautifulSoup` library, data storage using `MySQL`, and analysis using Python's `Pandas`, `Matplotlib`, and `Seaborn`. The code structure is as follows:

## Web Scraping with BeautifulSoup

- Data was scraped from IMDb using the `requests` library to fetch HTML content and `BeautifulSoup` to parse and extract relevant movie details (e.g., titles, ratings, genres, etc.).
- The data was then cleaned and structured into a usable format.

## Data Storage with MySQL

- The scraped data was stored in a MySQL database using Python's `mysql-connector` library. A relational schema was created to store movie information and their associated genres, ratings, and other metadata.

## Data Analysis with Pandas

- The stored data was extracted and loaded into `Pandas` DataFrames for cleaning, manipulation, and analysis. Various operations were performed, such as grouping data by genre, calculating average ratings, and analyzing trends over time.

## Visualization with Matplotlib and Seaborn

- Visualizations were created using `Matplotlib` and `Seaborn` to display trends in movie ratings, popularity, and genre performance. Graphs such as bar charts, scatter plots, and heatmaps were generated to illustrate key findings.

# Licensing and Credits

## IMDb Data
The IMDb dataset was accessed through web scraping, adhering to IMDb's terms of service and usage guidelines. Please note that scraping IMDb data for commercial purposes may require special permissions.

## Libraries and Tools
- **BeautifulSoup**: Used for parsing HTML and extracting data from IMDb.
- **Pandas**: Utilized for data manipulation and analysis.
- **Matplotlib**: Used for creating static visualizations.
- **Seaborn**: Employed to enhance the aesthetics of visualizations.
- **MySQL**: A relational database used for storing and querying the movie data.

## Code License
The code provided in this project is licensed under the MIT License, allowing users to freely use, modify, and distribute the code with proper attribution.

## Acknowledgments
The project is built on open-source tools and libraries, and we thank their developers for providing these invaluable resources. Special thanks to the contributors of BeautifulSoup, Pandas, Matplotlib, Seaborn, and MySQL Connector for their contributions to the Python ecosystem.



## How to Run the Project

To run this project, follow the steps below:

**Clone the repository**:
   First, clone the project repository to your local machine:
   ```bash
   git clone https://github.com/Clarkson-Applied-Data-Science/berhe-nyamuchengwa-big_data
   cd berhe-nyamuchengwa-big_data

pip install -r requirements.txt

python scripts/webscrapper.py
-This script extracts movie data from IMDb and saves it as movies_data.json and movies_data.csv in the root directory.

python scripts/scrapped_to_csv.py
-This script saves the data we scrapped from the website incsv format

python scripts/mergingdata.py
-Combines the scrapped data and data from kaggle.

python scripts/datacleaning.py
-This step handles duplicates, fills missing values, and formats the data after integration

python scripts/database.py
-Set up the MySQL database structure by running the script,This creates the necessary tables in MySQL database to store movie data.

python scripts/data_insertion.py
-This populates the database with structured movie data, ready for analysis

python scripts/analysis.py
-This script queries the database and produces visualizations or summaries of trends.























