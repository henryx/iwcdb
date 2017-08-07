/*
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
*/

CREATE TABLE lk_stato_serie(stato_serie VARCHAR(10) NOT NULL,
                            CONSTRAINT pk_lk_stato_serie PRIMARY KEY(stato_serie)
);

CREATE TABLE lk_editore(nome_editore VARCHAR(50) NOT NULL,
                        sede_editore VARCHAR(100),
                        CONSTRAINT pl_lk_editore PRIMARY KEY(nome_editore)
);

CREATE TABLE lk_collana(nome_collana VARCHAR(100) NOT NULL,
                        nome_editore VARCHAR(50),
                        CONSTRAINT pk_lk_collana PRIMARY KEY(nome_collana)
);

CREATE TABLE lk_serie(nome_serie   VARCHAR(100) NOT NULL,
                      nome_collana VARCHAR(100),
                      stato_serie  VARCHAR(10),
                      CONSTRAINT pk_lk_serie PRIMARY KEY(nome_serie)
);

CREATE TABLE ft_albo(numero_albo INTEGER,
                     nome_serie  VARCHAR(100),
                     data_uscita DATE,
                     prezzo      NUMERIC(11,2),
                     valuta      VARCHAR(3) DEFAULT 'EUR'
);