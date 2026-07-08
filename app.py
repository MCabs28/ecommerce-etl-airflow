from database.db_connection import get_connection


def main():
    conn = get_connection()

    print("Connected to PostgreSQL!")

    conn.close()


if __name__ == "__main__":
    main()
