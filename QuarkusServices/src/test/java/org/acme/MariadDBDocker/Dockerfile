# Utiliser l'image officielle de MariaDB
FROM mariadb:latest

# Définir les variables d'environnement pour MariaDB
ENV MARIADB_ROOT_PASSWORD=password
ENV MARIADB_DATABASE=log
ENV MARIADB_USER=user
ENV MARIADB_PASSWORD=password

# Exposer le port 3306
EXPOSE 3306

COPY ./init.sql /docker-entrypoint-initdb.d/
