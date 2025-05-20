# Toteutusraportti
Ohjelma on toteutettu Python kielellä, ja sen käyttöliittymä hyödyntää Pygame-kirjastoa.

## Rakenne
Ohjelma luo luolaston annettujen parametrien pohjalta (config.py tiedosto) luoden satunnaisen mallisia huoneita, joiden väliset käytävät luodaan Bowyer-Watson algoritmin luomien triangulaatioiden pohjalta. Triangulaatioiden kaariin perustuvia huoneiden välisiä käytäviä karsitaan edelleen Primin algoritmin virittän puun avulla. Ohjelma käyttää A* algoritmia laskemaan lyhimmän reitin pelaajan ja maalin välillä.

## Aikavaativuudet
Ohjelma käyttää Bowyer–Watson-algoritmia käytävien luomiseen ja Prim’n algoritmia niiden karsimiseen. Bowyer–Watson muodostaa Delaunay-triangulaation, joka yhdistää huoneet kolmioverkoksi keskimäärin ajassa O(n log n) pahimman tapauksen ollessa O(n^2). Tämän jälkeen Prim’n algoritmilla valitaan verkosta lyhin mahdollinen yhdistelmä käytäviä (eli pienin virittävä puu) myös toimii ajassa O(n log n). Kokonaisuudessaan ohjelman aikavaativuus on keskimäärin O(n log n). Pelin suorituskyvyn kannalta tällä ei ole suurta merkitystä kun luolaston luominen tapahtuu ennen varsinaista peli tapahtumaa.

## Jatkokehitys
A* käyttö monipuolisempien ja luonnollisempien käytävien piirtämiseen olisi oletettavasti nopeasti toteutettava lisäominaisuus A* algoritmin ollessa jo osa ohjelmaa. Käytävien määrän lisääminen niin että kaikkia Primin algoritmin pistamia käytäviä ei poistetakkaan luolastosta. Myös alun perin toteuttavaksi tarkoitettu luolaston kerroksellisuus toisi ohjelman käyttöön monipuolisuutta.


## Kielimallien käyttö
ChatGPT (4o) on käytetty apuna tiedon etsinässä, selittämään käsitteitä sekä erityisesti selittämään pygamen toiminnallisuuksia.



## Lähteet

[Wikipedia: Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)

[Wikipedia: Bowyer–Watson algorithm](https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm)

[Wikipedia: Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)

[Wikipedia: A* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)

[Vazgriz.com: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/)

[Emergent blog: Dungeon generation — from simple to complex](https://tiendil.org/en/posts/dungeon-generation-from-simple-to-complex)
