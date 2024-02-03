# pip install mysql-connector-python

import mysql.connector

def get_connection():
    conn = mysql.connector.connect(host="localhost", user="test", password="vertic06", db="test")
    cursor = conn.cursor(buffered=True, dictionary=True)
    return cursor, conn

'''

CREATE DATABASE test DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_520_ci;
GRANT ALL ON test.* TO test@localhost IDENTIFIED BY 'pwd';

CREATE TABLE `stocks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt_stamp` date NOT NULL,
  `closing` float(15,2) NOT NULL,
  `symbol` varchar(4) COLLATE utf8mb4_unicode_520_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dt_stamp` (`dt_stamp`),
  KEY `symbol` (`symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci

INSERT INTO stocks (id, dt_stamp, closing, symbol) VALUES (1, '1970-01-01', 100.00, 'AAPL');
INSERT INTO stocks (id, dt_stamp, closing, symbol) VALUES (2, '1970-01-02', 200.00, 'GOOG');

'''
