-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS pp_dev_db;
CREATE USER IF NOT EXISTS 'pp_user'@'localhost' IDENTIFIED BY 'pp_PWD_167,@9uri0';
GRANT ALL PRIVILEGES ON `pp_dev_db`.* TO 'pp_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pp_user'@'localhost';
FLUSH PRIVILEGES;
