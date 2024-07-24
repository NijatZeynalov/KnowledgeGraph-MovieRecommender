import pandas as pd
import json

def load_tmdb_data(movies_path, credits_path):
    tmdb_movies_df = pd.read_csv(movies_path)
    tmdb_credits_df = pd.read_csv(credits_path)
    return tmdb_movies_df, tmdb_credits_df

def preprocess_tmdb_data(tmdb_movies_df, tmdb_credits_df):
    # Select relevant columns
    tmdb_movies_df = tmdb_movies_df[['id', 'title', 'genres']]
    tmdb_credits_df = tmdb_credits_df[['movie_id', 'title', 'cast', 'crew']]

    # Function to parse JSON columns safely
    def parse_json_column(column):
        try:
            return json.loads(column.replace("'", "\""))
        except json.JSONDecodeError:
            return []

    # Clean 'genres' column
    tmdb_movies_df.loc[:, 'genres'] = tmdb_movies_df['genres'].apply(lambda x: [genre['name'] for genre in parse_json_column(x)])

    # Clean 'cast' column to include only the first 2 actors
    tmdb_credits_df.loc[:, 'cast'] = tmdb_credits_df['cast'].apply(lambda x: [actor['name'] for actor in parse_json_column(x)[:2]])

    # Clean 'crew' column to include only directors
    tmdb_credits_df.loc[:, 'crew'] = tmdb_credits_df['crew'].apply(lambda x: [member['name'] for member in parse_json_column(x) if member['job'] == 'Director'])

    # Merge datasets
    merged_df = pd.merge(tmdb_movies_df, tmdb_credits_df, left_on='id', right_on='movie_id')
    merged_df = merged_df[['movie_id', 'title_x', 'genres', 'cast', 'crew']]
    merged_df.columns = ['movie_id', 'title', 'genres', 'cast', 'crew']

    return merged_df