# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS
# UNTESTED. USERDATABASE IS A WORK IN PROGRESS




sudo docker pull postgres

sudo docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres

sudo docker run -it --rm --network locnetwork postgres psql -h some-postgres -U postgres

docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres
sudo docker run --name pg-docker --network locnetwork -e POSTGRES_PASSWORD=docker -d -p 5432:5432  postgres


docker run -d \
    --name some-postgres \
    -e POSTGRES_PASSWORD=mysecretpassword \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    postgres









# JBS 
sudo docker exec -it jbscont /bin/bash
