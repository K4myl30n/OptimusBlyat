CREATE TABELE premia (
    id VARCHAR(20) PRIMARY KEY,
    premia NUMERIC
);

CREATE TABELE dzial (
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(20),
    siedziba VARCHAR(20)
);

CREATE TABELE pracownicy (
    id VARCHAR(6) PRIMARY KEY,
    nazwisko VARCHAR(40),
    imie VARCHAR(20)
    stanowisko VARCHAR(20)
    data_zatrudnienia VARCHAR(23)
    placa NUMERIC,
    premia NUMERIC,
    id_dzial INTEGER,
    FOREIGN KEY(stanowisko) REFERENCES premia(id),
    FOREIGN KEY(id_dzial) REFERENCES dzial(id)
);
