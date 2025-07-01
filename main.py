import os
import pandas as pd
from google.cloud import bigquery

# 1. Authenticate with service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:/Users/chill/Downloads/datapro-457706-5cf7274447ac.json'
client = bigquery.Client()

# 2. Project and dataset info
project_id = client.project
dataset_id = "datapro-457706.demodataset"

# 3. Load the main CSV file
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

# 5. Merge everything to build the fact table (excluding country)
df_fact = df \
    .merge(dim_movie, on=['Title', 'Year', 'Duration', 'Content_Rating', 'Description']) \
    .merge(dim_director, on='Director') \
    .merge(dim_actor, on='Lead_Actor') \
    .merge(dim_language, on='Language')

# 6. Select only required columns for the fact table (excluding country_id)
fact_movie_performance = df_fact[[ 
    'movie_id', 'director_id', 'actor_id', 'language_id',
    'Rating', 'Votes', 'Num_Awards', 'Critic_Reviews'
]]

# 7. Upload to BigQuery
table_id = f"{dataset_id}.movies_facts"
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_TRUNCATE",
    schema=[
        bigquery.SchemaField("movie_id", "INT64"),
        bigquery.SchemaField("director_id", "INT64"),
        bigquery.SchemaField("actor_id", "INT64"),
        bigquery.SchemaField("language_id", "INT64"),
        bigquery.SchemaField("Rating", "FLOAT64"),
        bigquery.SchemaField("Votes", "INT64"),
        bigquery.SchemaField("Num_Awards", "INT64"),
        bigquery.SchemaField("Critic_Reviews", "INT64"),
    ]
)

job = client.load_table_from_dataframe(fact_movie_performance, table_id, job_config=job_config)
job.result()

print("✅ movies_facts table loaded successfully (without country_id).")