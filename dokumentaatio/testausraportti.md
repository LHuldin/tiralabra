# Testausraportti
Projektin testauksessa on keskitytty erityisesti algoritmien toteutukseen ja niitä on pyritty testaamaan kattavasti yksikkötesteillä. Käyttöliittymään ja pygameen liittyvät toiminnallisuudet ovat kommentoitu pois testikattavuudesta.

Ohessa lopullinen Coveragen luoma testikattavuus raportti, joka pyrki osoittamaan tarvittavan kattavuuden testien haarautumiskattavuudelle. Tiedost astar.py sisältää A* algoritmin toteutuksen ja paths.py Bowyer-Watson ja Prim algoritmien toteutuksen.
![Testikattavuus](https://github.com/LHuldin/tiralabra/raw/main/dokumentaatio/img/Näyttökuva%202025-05-21%20kello%201.35.43.png)

A* algoritmin osalta testataan Manhattan-etäisyyden laskeminen, naapuri ruutujen tarkastaminen ja viiden askeleen pituisen polun rakentaminen. lisäksi testataan algoritmin toimintaa esteettömässä ruudukossa, ruudukossa maaliin ei ole mahdollista päästä ja tilannetta jossa lähtöruutu ja maali ovat sama piste.

Bowyer-Watson algoritmin osalta testataan ensimmäiseksi, että Edge-luokan osalta reuna on sama riippumatta siitä, missä järjestyksessä pisteet annetaan, ja että hajautus toimii oikein. Toisessa testissä testataan Triangle-luokan kehäympyrän laskemista, tarkistetaan kolmion keskipiste ja säteen neliö muodostuvat oikein. Kolmas testi testaa algoritmin toimintaa niin että neljästä pisteestä muodostetusta neliöstä muodostuu kaksi kolmiota ja kaikki alkuperäiset pisteet löytyvät näistä kolmioista. neljännessä testissä testataan että aluksi muodostetun super kolmion osia ei ole enää lopullisten kolmioiden joukossa. viides ja kuudes testi tarkastavat että mikäli pisteet ovat samalla suoralla, ei kolmioita muodostu. 

Primin algoritmin osalta testataan että pienin virittävä puu muodostuu oikein annetulla syötteellä ja että distance funktio laskee oikein euklidisen etäisyyden. testit testaavat myös että Prim palauttaa tyhjällä syötteellä tyhjän listan.

Ohjelman käyttöliittymää voi tällä hetkellä testata muutamalla painikkeella, jotka luovat uuden pohjan, kartan ruutujakoa havainnollistavan ruudukon. Painikkeilla on myös mahdollisuus saada näkyviin jokaisesta huoneesta toiseen johtavat linjat, sekä Bowyer-Watson algoritmia hyödyntävän polkujen luonnin joka luo linjat tämän triangulaation mukaisesti, sekä Primin algoritmiin perustuvan karsitun version näistä triangulaatioiden kaarista. 
