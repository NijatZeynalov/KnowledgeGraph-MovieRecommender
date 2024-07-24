# KnowledgeGraph MovieRecommender

## Overview

This project demonstrates the creation and utilization of a knowledge graph to enhance movie recommendation systems. The knowledge graph is built using the TMDB 5000 Movie Dataset, which includes metadata such as genres, cast, crew, and production companies. The graph structure provides a rich, interrelated representation of the data, allowing for more informed and personalized recommendations.

## What is a Knowledge Graph?

A knowledge graph is a structured representation of data where entities (such as movies, actors, directors) are nodes, and the relationships between them (such as "acted in," "directed by") are edges. 

Knowledge graphs provide additional context that can enhance the capabilities of a recommendation system:

* Entity Relationships: By understanding the relationships between entities, the system can make more informed recommendations. For example, if a user likes movies directed by "John Lasseter," the system can recommend other movies directed by him.

* Attribute Similarity: The system can recommend movies that share similar attributes (e.g., genre, actors, directors).

![knowledge_graph](https://github.com/user-attachments/assets/d571785b-b665-4bf4-ab18-1477d26936ec)


## Setup and Usage


Python 3.9+

Clone the repository:

```
git clone https://github.com/yourusername/KnowledgeGraph-MovieRecommender.git
cd KnowledgeGraph-MovieRecommender
```
Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


Install the required packages:

```
pip install -r requirements.txt
```

Running the Project

```
python src/main.py
```


