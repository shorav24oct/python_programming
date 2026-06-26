create table Labour (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    wage int,
    role varchar(50),
    email varchar(100) unique not null
);