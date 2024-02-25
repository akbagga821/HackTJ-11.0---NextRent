DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS homescapes;

CREATE TABLE users (
    c_email TEXT PRIMARY KEY,
    c_name TEXT,
    c_pass TEXT,
    c_home1 TEXT,
    c_home2 TEXT,
    c_home3 TEXT
);


CREATE TABLE homescapes (
    h_name TEXT PRIMARY KEY,
    h_users ARRAY,
    h_utilities ARRAY,
    h_groceries ARRAY,
    h_outings ARRAY,
    h_other ARRAY
);