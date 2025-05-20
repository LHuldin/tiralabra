# Toteutusraportti
Ohjelma on toteutettu Python kielellä, ja sen käyttöliittymä hyödyntää Pygame-kirjastoa.

## Rakenne
Ohjelma luo luolaston annettujen parametrien pohjalta (config.py tiedosto) luoden satunnaisen mallisia huoneita, joiden väliset käytävät luodaan Bowyer-Watson algoritmin luomien triangulaatioiden pohjalta. Triangulaatioiden kaariin perustuvia huoneiden välisiä käytäviä karsitaan edelleen Primin algoritmin virittän puun avulla. Ohjelma käyttää A* algoritmia laskemaan lyhimmän reitin pelaajan maalin välillä.

## Jatkokehitys
A* käyttö monipuolisempien ja luonnollisempien käytävien piirtämiseen olisi oletettavasti nopeasti toteutettava lisäominaisuus A* algoritmin ollessa jo osa ohjelmaa. Käytävien määrän lisääminen niin että kaikkia Primin algoritmin pistamia käytäviä ei poistetakkaan luolastosta. Myös alun perin toteuttavaksi tarkoitettu luolaston kerroksellisuus toisi ohjelman käyttöön monipuolisuutta.


## Kielimallien käyttö
ChatGPT (4o) on käytetty apuna tiedon etsinässä, selittämään käsitteitä sekä selittämään pygamen toiminnallisuuksia.



## Lähteet

[Wikipedia: Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)

[Wikipedia: Bowyer–Watson algorithm](https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm)

[Vazgriz.com: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/)

[Emergent blog: Dungeon generation — from simple to complex](https://tiendil.org/en/posts/dungeon-generation-from-simple-to-complex)
