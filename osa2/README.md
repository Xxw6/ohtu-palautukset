# Osan 2 tehtävät 4–8

Pohjakoodi: https://github.com/ohjelmistotuotanto-jyu/tehtavat

- Riippuvuuksien injektoinnissa olio saa tarvitsemansa riippuvuuden
  konstruktorissa. NHL-palvelun testit käyttävät oikean verkkolukijan sijaan
  kiinteän pelaajalistan palauttavaa stubia.
- NHL-palvelun haarautumakattavuus mitataan coverage-työkalulla.
  Pohjan top(n) palauttaa n+1 pelaajaa; tämä alkuperäinen toiminta on säilytetty.
- pytest on kehitysriippuvuus: sitä tarvitaan testien ajamiseen, ei sovelluksen
  normaaliin käyttöön. jsonpickle asennetaan, lukitaan versioon 2.2.0 ja poistetaan.
- Semanttisen version pääluvun muutos voi sisältää rikkovia muutoksia.
  Päivitys 2.2.0 -> 3.2.2 ylittää pääversion rajan; 3.0.3 -> 3.2.2 ei ylitä.
- TOML-lukija käyttää tomli-kirjastoa ja lukee PEP 621 -projektitiedot sekä
  kehitysriippuvuudet dependency-groups-osiosta.
- ChatGPT:tä käytettiin toteutuksessa ja virheiden selvittämisessä.

Tarkistukset: suorita repositorion juuressa `bash tarkista.sh`.
