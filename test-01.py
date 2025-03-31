import psycopg2

def list_postgres_databases():
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the query to list all databases
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")

        # Fetch all the results
        databases = cursor.fetchall()

        # Print the list of databases
        for db in databases:
            print(db[0])

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Call the function
list_postgres_databases()