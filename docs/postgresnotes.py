import psycopg2

import secrets

# I need to connect to a user database that stores credentials

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


sudo docker run -t -d --name pg pgcont
sudo docker exec -it  pg /bin/bash
apt-get install sudo
# START POSGRESQL FROM FRESH INSTALL
sudo service postgresql start
sudo -i -u postgres
psql
create database testdb;
create user locustscriptuser with encrypted password 'locustpassword';
grant all privileges on database testdb to locustscriptuser;

CREATE TABLE public.user_credential(
   ID           SERIAL PRIMARY KEY     NOT NULL,
   username       VARCHAR(50)    NOT NULL,
   password       VARCHAR(50)     NOT NULL
);


INSERT INTO public.user_credential (username, password)
VALUES
    ('testlocust01', 'Turing123'),
    ('testlocust02', 'Turing123'),
    ('testlocust03', 'Turing123'),
    ('testlocust04', 'Turing123'),
    ('testlocust05', 'Turing123'),
    ('testlocust06', 'Turing123'),
    ('testlocust07', 'Turing123'),
    ('testlocust08', 'Turing123'),
    ('testlocust09', 'Turing123')
;
