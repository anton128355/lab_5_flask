DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    transmission TEXT NOT NULL,
    year TEXT NOT NULL,
    power TEXT NOT NULL,
    fuel TEXT NOT NULL,
    mileage TEXT NOT NULL,
    price TEXT NOT NULL,
    photo TEXT NOT NULL
);