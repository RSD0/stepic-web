DROP DATABASE IF EXISTS `djangodb`;
CREATE DATABASE `djangodb`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'mysql';
CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON djangodb.* TO 'django'@'localhost' IDENTIFIED BY 'pass'

WITH GRANT OPTION;
FLUSH PRIVILEGES;