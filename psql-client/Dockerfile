FROM debian:stable

RUN apt update && apt upgrade -y && apt install postgresql-client -y


COPY psql-client/testname.csv /tmp
COPY psql-client/initialize /tmp
