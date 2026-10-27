from sqlalchemy import text

from app.db.database import engine


def check_database_connection():
    query = text("""
        SELECT
            current_database() AS database_name,
            current_schema() AS current_schema,
            version() AS postgres_version
    """)

    try:
        with engine.connect() as connection:
            result = connection.execute(query).mappings().one()

            print("Database connection successful!")
            print(f"Database name: {result['database_name']}")
            print(f"Current schema: {result['current_schema']}")
            print(f"PostgreSQL version: {result['postgres_version']}")

            tables_query = text("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'quizonics'
                  AND table_type = 'BASE TABLE'
                ORDER BY table_name
            """)

            tables = connection.execute(tables_query).scalars().all()

            print("\nTables in the quizonics schema:")

            if tables:
                for table in tables:
                    print(f"- {table}")
            else:
                print("No base tables found in the quizonics schema.")

    except Exception as exc:
        print("Database verification failed.")
        print(f"Error type: {type(exc).__name__}")
        print(str(exc))

    finally:
        engine.dispose()


if __name__ == "__main__":
    check_database_connection()