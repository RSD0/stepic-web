#!/usr/bin/env bash

mysql -u root -e "CREATE DATABASE djangodb;"
mysql -u root -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass';"
mysql -u root -e "GRANT ALL ON djangodb.* TO 'django@localhost';"
mysql -u root -e "FLUSH PRIVILEGES;"