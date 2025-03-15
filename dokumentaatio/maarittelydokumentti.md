# Määrittelydokumentti

Tämä dokumentti on Helsingin Yliopiston Tietojenkäsittelytieteen kandiohjelman aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssin harjoitustyön määrittelydokumentti.

Suoritan kurssin osana tietojenkäsittelytieteen kandiohjelmaa (TKT).

## Aihe

Harjoitustyön aiheena luolastojen generointi. Ohjelmassa käyttäjä antaa syötteenä pinta-alan jonka sisään luolasto generoidaan sekä mahdollisesti eri tasojen/kerrosten määrän.

Aiheen varsinaninen ydin on algoritmit jotka luovat luolaston ja erityisesti sen osat kuten huoneet ja niiden väliset käytävät.

## Ohjelmointikieli

Ohjelma toteutetaan käyttäen Pythonia. Riippuvuuksien hallinta toteutetaan Poetryn avulla. Ohjelman testaus toteutetaan Pythonin sisäisen unittest kehyksen kautta mutta ohjelman ja algoritmien testaus tarvitsee oletettavasti muitakin testausmenetelmiä kuin vain unittest yksikkötestit.

## Algoritmit

Luolaston osien (huoneiden) keskinäiseen sijoittumiseen käytetään delaunay triangulaatioiden laskemiseen käytettävää algoritmiä kuten Bowyer–Watson algoritmiä. 
Kyseisen algoritmin aikavaatimukset ovat tutkimieni lähteiden mukaan pahimmassa tapauksessa O(n²) mutta pääasiassa aikavaatimuksen ollessa O(n log n).
Ohjelma tulee Bowyer–Watson algoritmin lisäksi todennäköisesti hyödyntämään jotakin vielä määriitelemätöntä algoritmiä osana luolaston generointia.


## Ohjelman ja dokumentaation kieli

Ohjelman koodi ja muuttujat ovat englanniksi mutta koodin kommentointi sekä muu dokumentaatio ovat suomeksi.


## Lähteet

[Wikipedia: Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)

[Wikipedia: Bowyer–Watson algorithm](https://en.wikipedia.org/wiki/Bowyer–Watson_algorithm)

[Vazgriz.com: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/))
