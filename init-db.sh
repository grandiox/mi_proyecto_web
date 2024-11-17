#!/bin/bash
set -e

mysql -u root -p"$MYSQL_ROOT_PASSWORD" <<-EOSQL
    CREATE DATABASE IF NOT EXISTS app_db;
    CREATE USER IF NOT EXISTS 'dbuser'@'%' IDENTIFIED BY 'dbpass123';
    GRANT ALL PRIVILEGES ON app_db.* TO 'dbuser'@'%';
    FLUSH PRIVILEGES;

    USE app_db;
    
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
EOSQL
