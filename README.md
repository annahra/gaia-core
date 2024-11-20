# Gaia Core - Development Environment Setup

Welcome to **Gaia Core**, the backend service that powers the Gaia Atlas web application. This guide will walk you through setting up the development environment for Gaia Core, including how to run the necessary databases using Docker and configure your Python environment.

## Table of Contents

1. Prerequisites
2. Getting Started
3. Running the Databases
4. Seeding the Databases
5. Verifying the Setup
6. Common Issues

## Prerequisites

Before getting started, ensure that you have the following installed:

- Python 3.10+
- Docker and Docker Compose
- Docker Desktop (required for Docker to run on macOS)
- Homebrew (for package management on macOS)

### Additional macOS Requirement

To install `psycopg2-binary`, you need the `pg_config` tool, which comes with PostgreSQL. On macOS, you can install it using:

```bash
brew install postgresql
```

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/gaia-core.git
   cd gaia-core
   ```

2. **Set Up the Python Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS and Linux
   ```

3. **Install Dependencies**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

   > **Note**: If you encounter an error installing `psycopg2-binary`, make sure you have installed PostgreSQL with `brew install postgresql` to include the `pg_config` tool.

## Running the Databases

Ensure **Docker Desktop** is running on your machine. Then start the PostGIS and Neo4j databases:

```bash
docker-compose up -d
```

> **Note**: Wait for about a minute after running `docker-compose up` to ensure that the containers are fully up and running before seeding the databases.

- **PostGIS** will be accessible at `localhost:5432`.
- **Neo4j** will be accessible at `localhost:7474` (web interface) and `localhost:7687` (Bolt protocol).

## Seeding the Databases

To seed the databases with initial data, run the `seed.py` script:

```bash
python3 -m app.db.seed
```

This script will insert test data into both PostGIS and Neo4j databases.

## Verifying the Setup

### Check PostGIS

1. **Connect using `psql`**:

   ```bash
   psql -h localhost -U user -d gaia_db
   ```

   Run:

   ```sql
   SELECT * FROM air_quality_stations;
   ```

2. **Using pgAdmin or DBeaver**:
   Connect to `localhost:5432` and inspect the `air_quality_stations` table.

### Check Neo4j

1. **Open the Neo4j Browser**:
   Navigate to `http://localhost:7474` and log in using your credentials.
2. **Run a Cypher query**:
   ```cypher
   MATCH (n) RETURN n LIMIT 10;
   ```

## Common Issues

- **`ModuleNotFoundError: No module named 'app'`**:
  Run your scripts as modules from the project root:

  ```bash
  python3 -m app.db.seed
  ```

- **Error with `psycopg2-binary` installation**:
  Ensure you have `pg_config` installed by running:
  ```bash
  brew install postgresql
  ```

## Additional Notes

- **Environment Variables**: Configure sensitive data using environment variables or a `.env` file.
- **Cleaning Up Docker**:
  ```bash
  docker-compose down
  ```

This will stop and remove the containers but preserve the volumes, so your data remains intact.
