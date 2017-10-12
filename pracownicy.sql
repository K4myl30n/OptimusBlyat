CREATE TABELE premia (
    id VARCHAR(20) PRIMARY KEY,
    premia NUMERIC
);


CREATE TABELE dzial (
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(40),
    siedziba VARCHAR(40)
);


CREATE TABELE pracownicy (
    id VARCHAR(6) PRIMARY KEY,
    nazwisko VARCHAR(20),
    imie VARCHAR(20)
    stanowisko VARCHAR(20)
    data_zatrudnienia VARCHAR(23)
    placa NUMERIC,
    id_dzial INTEGER,
    premia NUMERIC DEFAULT 0,
    FOREIGN KEY(stanowisko) REFERENCES premia(id),
    FOREIGN KEY(id_dzial) REFERENCES dzial(id)
);
