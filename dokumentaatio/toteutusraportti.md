# Toteutusraportti

## Toiminta ja käyttöliittymä
Ohjelma on toteutettu Python kielellä, ja sen käyttöliittymä hyödyntää Pygame-kirjastoa. 

Ohjelma on peli, jossa pelaaja liikuttaa hahmoa satunnaisesti luodussa luolastossa pyrkien löytämään maalin. Vihjeenä maalin sijainnista pelaaja näkee jatkuvasti päivittyvän laskurin joka ilmoittaa lyhimmän etäisyyden sallittuja reittejä pitkin pelaajan ja maalin välillä.

## Rakenne
Ohjelma luo luolaston annettujen parametrien pohjalta (config.py tiedosto) luoden satunnaisen mallisia huoneita, joiden väliset käytävät luodaan Bowyer-Watson algoritmin luomien triangulaatioiden pohjalta. Triangulaatioiden kaariin perustuvia huoneiden välisiä käytäviä karsitaan edelleen Primin algoritmin virittän puun avulla. Ohjelma käyttää A* algoritmia laskemaan lyhimmän reitin pelaajan ja maalin välillä ja päivittää tätä tietoa jatkuvasti pelaajan liikkuessa luolastossa.

## Aikavaativuudet
Ohjelma käyttää Bowyer–Watson-algoritmia käytävien luomiseen ja Prim’n algoritmia niiden karsimiseen. Bowyer–Watson muodostaa Delaunay-triangulaation, joka yhdistää huoneet kolmioverkoksi keskimäärin ajassa O(n log n) pahimman tapauksen ollessa kuitenkin O(n^2). Tämän jälkeen Primin algoritmilla valitaan verkosta lyhin mahdollinen yhdistelmä käytäviä (eli pienin virittävä puu) myös toimii ajassa O(n log n). 

Jatkuvaan etäisyyden päivittämiseen käytettävän A* algoritmin aika vaativuus on pahimman tapauksen osalta O(n).    

## Jatkokehitys
A* käyttö monipuolisempien ja luonnollisempien käytävien piirtämiseen olisi oletettavasti nopeasti toteutettava lisäominaisuus, A* algoritmin ollessa jo osa ohjelmaa. Käytävien määrän lisääminen niin että kaikkia Primin algoritmin poistamia käytäviä ei poistetakkaan luolastosta. Myös alun perin toteuttavaksi tarkoitettu luolaston kerroksellisuus toisi ohjelman käyttöön monipuolisuutta. 

Koodin rakenteen osalta olisi selkeämpää jos paths.py tiedoston jakamisisi osiin jotta Bowyer-watson ja Primin algoritmi olisivat erillisissä tiedostoissa.


## Kielimallien käyttö
ChatGPT (4o ja 4.5) on käytetty apuna tiedon etsinässä, virheiden etsinnässä, selittämään käsitteitä sekä erityisesti selittämään pygamen toiminnallisuuksia.



## Lähteet

[Wikipedia: Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)

[Wikipedia: Bowyer–Watson algorithm](https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm)

[Wikipedia: Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)

[Wikipedia: A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Vazgriz.com: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/)

[Emergent blog: Dungeon generation — from simple to complex](https://tiendil.org/en/posts/dungeon-generation-from-simple-to-complex)

[Game Developer: Procedural Dungeon Generation Algorithm](https://www.gamedeveloper.com/programming/procedural-dungeon-generation-algorithm)
