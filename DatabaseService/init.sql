CREATE DATABASE IF NOT EXISTS Logs;
USE Logs;

CREATE TABLE LogTable(
    time VARCHAR(50),
    calculus VARCHAR(50)
);

CREATE USER '${MARIADB_USER}'@'%' IDENTIFIED BY '${MARIADB_PASSWORD}';
GRANT ALL PRIVILEGES ON Logs.* TO '${MARIADB_USER}'@'%';
FLUSH PRIVILEGES;
