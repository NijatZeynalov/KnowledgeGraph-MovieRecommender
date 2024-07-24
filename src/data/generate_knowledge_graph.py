import pandas as pd
import rdflib
from rdflib import Graph, Literal, RDF, URIRef, Namespace
from urllib.parse import quote, unquote

def generate_knowledge_graph(df):
    g = Graph()
    ns = Namespace("http://example.org/")

    for index, row in df.iterrows():
        movie_uri = ns[f"movie/{row['movie_id']}"]
        g.add((movie_uri, RDF.type, ns.Movie))
        g.add((movie_uri, ns.title, Literal(row['title'])))

        for genre in row['genres']:
            genre_uri = ns[f"genre/{quote(genre)}"]
            g.add((movie_uri, ns.genres, genre_uri))

        for actor in row['cast']:
            actor_uri = ns[f"actor/{quote(actor)}"]
            g.add((movie_uri, ns.cast, actor_uri))

        for director in row['crew']:
            director_uri = ns[f"director/{quote(director)}"]
            g.add((movie_uri, ns.crew, director_uri))

    return g

def save_knowledge_graph(g, path):
    g.serialize(destination=path, format='turtle')