drop table if exists sensors;
    create table sensors (
        id integer primary key autoincrement,
        humidity integer null,
        barometric_pressure integer null,
        temperature integer null,
        time_stamp text null
    );