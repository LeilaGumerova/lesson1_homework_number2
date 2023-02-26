--
-- File generated with SQLiteStudio v3.4.3 on Вс фев 26 11:57:40 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Coffee
CREATE TABLE IF NOT EXISTS Coffee (ID INTEGER PRIMARY KEY UNIQUE, Sort TEXT, Power REAL, Grains TEXT, Taste TEXT, Price INTEGER, Volume INTEGER);
INSERT INTO Coffee (ID, Sort, Power, Grains, Taste, Price, Volume) VALUES (123, 'Araba chocolate', 0.8, 'True', 'Very tasty', 120, 120);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
