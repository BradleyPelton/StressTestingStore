# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS

import psycopg2

import secrets

# I need to connect to a user database that stores credentials

# try:
#     connection = psycopg2.connect(user=secrets.DATABASE_USER,
#                                   password=secrets.DATABASE_USER_PASSWORD,
#                                   host=secrets.DATABASE_HOST_IP,
#                                   port=secrets.DATABASE_PORT,
#                                   database="locustDB")

#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     print(connection.get_dsn_parameters(), "\n")

#     # Print PostgreSQL version
#     cursor.execute("SELECT * FROM user_credential;")
#     # record = cursor.fetchone()
#     records = cursor.fetchall()
#     print(records)

# except (Exception, psycopg2.Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     # closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

def select_all_users():
    """return a dictionary of all rows in the user_credentials table"""
    try:
        connection = psycopg2.connect(user=secrets.DATABASE_USER,
                                      password=secrets.DATABASE_USER_PASSWORD,
                                      host=secrets.DATABASE_HOST_IP,
                                      port=secrets.DATABASE_PORT,
                                      database="locustDB")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")

        # Print PostgreSQL version
        cursor.execute("SELECT * FROM user_credential;")
        records = cursor.fetchall()

        user_dict = {tup[1]: {'password': tup[2], 'cookies': ''} for tup in records}
        print(user_dict)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

select_all_users()