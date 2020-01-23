DROP TABLE IF EXISTS categories;

CREATE TABLE categories
(
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    name NEXT NOT NULL
);