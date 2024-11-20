import os
from dotenv import load_dotenv
import psycopg2
from neo4j import GraphDatabase

# Load environment variables from .env file
load_dotenv()

# PostgreSQL connection function using environment variables
def get_postgis_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("PostGIS connection established.")
        return conn
    except Exception as e:
        print(f"Error connecting to PostGIS: {e}")
        return None

# Neo4j driver instance using environment variables
neo4j_driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI", "bolt://localhost:7687"),
    auth=(
        os.getenv("NEO4J_USER", "neo4j"),
        os.getenv("NEO4J_PASSWORD", "password")
    )
)

def close_neo4j_driver():
    if neo4j_driver:
        neo4j_driver.close()
        print("Neo4j driver closed.")
