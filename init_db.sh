#!/usr/bin/env bash

mysql -uroot -e "CREATE DATABASE djangodb;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass';"
mysql -uroot -e "GRANT ALL ON djangodb.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"