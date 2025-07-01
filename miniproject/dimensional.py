import os
import pandas as pd
from google.cloud import bigquery

# 1. Set up authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:/Users/chill/Downloads/datapro-457706-5cf7274447ac.json"

# 2. Create BigQuery client
client = bigquery.Client()
dataset_id = "datapro-457706.demodataset"

# 3. Load the CSV
df = pd.read_csv(r"C:/sampleprogram/revature_daily_task/movie_genre_classification_final.csv")
df = df.head(100)

# 4. Create dimension tables
dim_movie = df[['Title', 'Year', 'Duration', 'Content_Rating', 'Description']].drop_duplicates().reset_index(drop=True)
dim_movie['movie_id'] = range(1, len(dim_movie) + 1)

dim_director = df[['Director']].drop_duplicates().reset_index(drop=True)
dim_director['director_id'] = range(1, len(dim_director) + 1)

dim_actor = df[['Lead_Actor']].drop_duplicates().reset_index(drop=True)
dim_actor['actor_id'] = range(1, len(dim_actor) + 1)

dim_language = df[['Language']].drop_duplicates().reset_index(drop=True)
dim_language['language_id'] = range(1, len(dim_language) + 1)

# 5. Upload dimension tables to BigQuery

# Upload dim_movie
client.load_table_from_dataframe(
    dim_movie[['movie_id', 'Title', 'Year', 'Duration', 'Content_Rating', 'Description']],
    f"{dataset_id}.dim_movie",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
).result()
print("✅ dim_movie uploaded")

# Upload dim_director
client.load_table_from_dataframe(
    dim_director[['director_id', 'Director']],
    f"{dataset_id}.dim_director",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
).result()
print("✅ dim_director uploaded")

# Upload dim_actor
client.load_table_from_dataframe(
    dim_actor[['actor_id', 'Lead_Actor']],
    f"{dataset_id}.dim_actor",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
).result()
print("✅ dim_actor uploaded")

# Upload dim_language
client.load_table_from_dataframe(
    dim_language[['language_id', 'Language']],
    f"{dataset_id}.dim_language",
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
).result()
print("✅ dim_language uploaded")
