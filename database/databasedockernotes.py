# HOST MACHINE
sudo ss -tulwn | grep LISTEN
# Check which ports are open
sudo pkill -u postgres
# kill any postgres instances hogging up port 5432



##########################
# CREATE A CONTAINER-NETWORK
sudo docker network create locnetwork



# CREATE NEW PG container
sudo docker run -t -d -p 5432:5432 --network locustnetwork --name pg pgcont
sudo docker run -t -d --network locnetwork --name pg pgcont
sudo docker exec -it  pg /bin/bash
apt-get install sudo
# START POSGRESQL FROM FRESH INSTALL
sudo service postgresql start
sudo -i -u postgres
psql
create database testdb;
create user locustscriptuser with encrypted password 'locustpassword';
grant all privileges on database testdb to locustscriptuser;



# CREATE NEW JBSCONT container
sudo docker run -t -d --name jbscont --network locnetwork bradleypelton/locustconfig1
sudo docker exec -it jbscont /bin/bash
apt-get install sudo
sudo apt-get install -y libpq-dev
sudo apt-get install -y nano
pip3 install psycopg2







# nano psy
import psycopg2

# I need to connect to a user database that stores credentials

try:
    connection = psycopg2.connect(user='locustscriptuser',
                                password='locustpassword',
                                host='pg',
                                port='5432',
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