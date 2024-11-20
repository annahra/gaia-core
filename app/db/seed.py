from app.db import get_postgis_connection, neo4j_driver, close_neo4j_driver

# Function to seed PostGIS
def seed_postgis():
    conn = get_postgis_connection()
    if conn:
        try:
            cur = conn.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS air_quality_stations (
                station_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                location GEOMETRY(POINT, 4326),
                parameter VARCHAR(10),
                value FLOAT,
                measurement_date TIMESTAMP
            );
            """
            cur.execute(create_table_query)
            sample_data = [
                ("Station A", -118.2437, 34.0522, "pm25", 15.4, "2024-11-17 08:00:00"),
                ("Station B", -122.4194, 37.7749, "no2", 18.7, "2024-11-17 08:30:00"),
            ]
            for name, lon, lat, parameter, value, date in sample_data:
                cur.execute("""
                    INSERT INTO air_quality_stations (name, location, parameter, value, measurement_date)
                    VALUES (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s, %s, %s);
                """, (name, lon, lat, parameter, value, date))
            
            conn.commit()
            cur.close()
            print("PostGIS seeding completed.")
        except Exception as e:
            print(f"Error during PostGIS seeding: {e}")
        finally:
            conn.close()
    else:
        print("Failed to establish PostGIS connection.")

# Function to seed Neo4j
def seed_neo4j():
    try:
        with neo4j_driver.session() as session:
            session.run("""
                CREATE (lion:Species {name: 'Lion', type: 'Predator'}),
                       (zebra:Species {name: 'Zebra', type: 'Prey'})
            """)
            session.run("""
                MATCH (lion:Species {name: 'Lion'}), (zebra:Species {name: 'Zebra'})
                CREATE (lion)-[:PREDATOR_OF]->(zebra)
            """)
            print("Neo4j seeding completed.")
    except Exception as e:
        print(f"Error during Neo4j seeding: {e}")

if __name__ == "__main__":
    seed_postgis()
    seed_neo4j()
    close_neo4j_driver()
