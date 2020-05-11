# CREATE NEW JBSCONT container
# apt-get install sudo
# sudo apt-get install libpq-dev
# sudo apt-get install nano
# pip3 install psycopg2

# nano psy

# TODO- FINISH EDITING THE FOLLOWING SCRIPT, WHAT IS THE HOST IP????
import psycopg2

import secrets

# I need to connect to a user database that stores credentials

try:
    connection = psycopg2.connect(user='locustscriptuser'
                                  password='locustpassword',
                                  host=,
                                  port=secrets.DATABASE_PORT,
                                  database="locustDB")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")