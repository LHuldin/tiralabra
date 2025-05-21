# Käyttöohje

## Asennus

1. Kloonaa projekti:

```
git clone git@github.com:LHuldin/tiralabra.git
```

2. Siirry juurihakemistoon:

```
cd tiralabra
```

3. Lataa tarvittavat riippuuvuudet:

```
poetry install
```

4. Aktivoi virtuaaliympäristö:
```
poetry shell
```

5. Käynnistä ohjelma:

```
python3 src/main.py
```

## Ohjelman käyttö

- Ohjelma luo automaattisesti luolaston

- Pelin alkaessa näkymä on rajattu 8 ruudun etäisyydelle pelaajasta, näkymän rajauksen voi poistaa käyttöliittymän Fog: ON/OFF näppäimestä.

- Pelinäkymä seuraa oletuksena pelaajaa, seuraamisen voi poistaa käyttöliittymän Follow: ON / OFF näppäimestä, jolloin näkymää voi liikuttaa WASD-näppäimillä.

- Pelaajaa voi liikuttaa nuolinäppäimillä.

- Distance to goal kertoo etäisyyden ruutuina lyhintä mahdollista reittiä pitkin maaliin.

- Pelaajan saavutettua maalin peli pyytää luomaan uuden luolaston New Map napin avulla.

- New Map näppäin generoi uuden luolaston

- Show Grid näppäin näyttää ruudukon kartan yllä

- Show Tri/MST näppäin näyttää joko Bowyer-Watson triangulaatioihin perustuvan viivaston huoneiden välillä, sekä uudelleen painamalla tästä Primin algoritmiä hyödyntävän karsitun viivaston.

- Show All Paths näppäin näyttää kaikki huoneiden väliset yhteydet viivoina

- Color näppäin näyttää luolaston käytävät ja huoneet, joko kokonaan ruskeana tai käytävät valkoisena ja huoneet satunnaisen eri värisinä.

- Quit näppäin lopettaa ohjelman suorittamisen.



