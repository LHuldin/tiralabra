# Määrittelydokumentti

Tietojenkäsittelytieteen kandiohjelman aineopintojen harjoitustyö: Algoritmit ja tekoäly -kurssin harjoitustyön määrittelydokumentti.

## Aihe

Harjoitustyön aiheena luolastojen generointi.
Aiheen varsinaninen ydin algoritmi joka luo luolaston ja niiden väliset yhteydet.

## Ohjelmointikieli

Ohjelma toteutetaan käyttäen Pythonia. Riippuvuuksien hallinta toteutetaan Poetryn avulla ja ohjelman testaus toteutetaan Pythonin sisäisen unittest kehyksen kautta.

## Algoritmit

Luolaston osien keskinäiseen sijoittumiseen käytetään delaunay triangulaatioiden laskemiseen käytettävää algoritmiä kuten Bowyer–Watson algoritmiä. Kyseisen algoritmin aikavaatimukset ovat tutkimieni lähteiden mukaan pahimmassa tapauksessa O(n²) ja parhaimmassa tapauksessa O(n) mutta pääasiassa aikavaatimuksen ollessa O(n log n).

## Ohjelman ja dokumentaation kieli

Ohjelman koodi ja muuttujat ovat englanniksi mutta koodin kommentointi sekä muu dokumentaatio ovat suomeksi.
