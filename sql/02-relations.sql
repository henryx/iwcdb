/*
Copyright (C) 2015 Enrico Bianchi (enrico.bianchi@gmail.com)
Project       Italian Web Comic Database
Description   A web application for reporting information about comics
              published in Italy
License       GPL version 2 (see LICENSE for details)
*/

ALTER TABLE lk_serie
    ADD CONSTRAINT fk_lk_serie_1
    FOREIGN KEY (stato_serie)
    REFERENCES lk_stato_serie(stato_serie);

ALTER TABLE lk_serie
    ADD CONSTRAINT fk_lk_serie_2
    FOREIGN KEY (nome_collana)
    REFERENCES lk_collana(nome_collana);

ALTER TABLE lk_collana
    ADD CONSTRAINT fk_lk_collana_1
    FOREIGN KEY (nome_editore)
    REFERENCES lk_editore(nome_editore);

ALTER TABLE ft_albo
    ADD CONSTRAINT fk_ft_albo_1
    FOREIGN KEY (nome_serie)
    REFERENCES lk_serie(nome_serie);