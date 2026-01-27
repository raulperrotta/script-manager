from pathlib import Path
import sqlite3
import sys


def check_db(path: Path, schema: dict):
    # validates db format if it exists
    if path.exists():
        schema_checker(path, schema)
    # creates db file if it does not exist
    else:
        db_creation(path, schema)


def db_creation(path: Path, schema: dict):
    # create & connect to the db
    con = sqlite3.connect(path)
    cur = con.cursor()

    for table, columns in schema.items():
        # turn columns dict into a string
        table_info = ", ".join([f"{column_name} {column_type}" for column_name, column_type in columns.items()])
        # create table with the table info
        cur.execute(f"CREATE TABLE {table} ({table_info})")

    # commit changes and close connection
    con.commit()
    con.close()

    
def schema_checker(path: Path, schema: dict):
    # connect to the db
    con = sqlite3.connect(path)
    cur = con.cursor()

    for table, expected_columns in schema.items():
        # verify table composition
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table,))
        if cur.fetchone() is None:
            print("ERROR: invalid schema'")
            con.close()
            sys.exit(1)

        # get existing colum structure in database. [1] is column name, [2] is column type
        cur.execute(f"PRAGMA table_info({table});")
        actual_columns = {column_info[1]: column_info[2] for column_info in cur.fetchall()}

        # compare expected schema with actual schema
        for column_name, column_type in expected_columns.items():
            # column name comparison
            if column_name not in actual_columns:
                print("ERROR: invalid schema")
                con.close()
                sys.exit(1)
            # column type comparison
            if actual_columns[column_name].upper() != column_type.split()[0].upper():
                print("ERROR: invalid schema")
                con.close()
                sys.exit(1)

    # close connection
    con.close()