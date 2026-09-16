# Ilmastovisio: talousseuranta v1

Paikallinen selainpohjainen talousseurantatyökalu hankkeelle J11721.

## Aloita tästä

1. Pura ZIP-paketti pysyvään kansioon omalle koneellesi.
2. Avaa **Ilmastovisio.html** selaimessa, tavallisessa selainikkunassa.
3. Valitse **Pääkirjan tuonti**, tuo XLSX- tai CSV-tiedostosi ja hyväksy esikatselu.
4. Tarkista palkkarivit **Tapahtumat**-näkymässä. Valitse **Asetukset**-näkymässä viimeinen kokonaan kirjattu kuukausi ennustetta varten.
5. Lisää hakemukset, päätökset ja saadut maksut **Rahoitus**-näkymässä. Päivitä samaa rahoituserää sen edetessä.

Käyttö ei vaadi asennuksia, internetyhteyttä, tunnuksia tai backend-palvelinta. Hankesuunnitelman asetukset ovat valmiina, mutta omat pääkirjat tuodaan itse. Projektipaketti ei sisällä alkuperäisiä liitteitä tai valmiiksi ladattuja taloustapahtumia.

## Säilytä tiedot

Tiedot tallentuvat tämän selaimen IndexedDB-tietokantaan. **Vie varmuuskopio** säännöllisesti. Selaimen tietojen tyhjentäminen voi poistaa taloustiedot. Pidä käyttämäsi HTML samassa paikassa ja vie varmuuskopio ennen päivitystä, tiedoston siirtämistä tai selainvaihtoa. **Palauta varmuuskopio** korvaa nykyiset tiedot vasta vahvistuksen jälkeen.

Sovellus ei lähetä taloustietoja verkkoon eikä lataa ulkoisia kirjastoja tai fontteja. JSON-varmuuskopio sisältää taloustietosi eikä ole salattu.

## Huomioi laskennassa

Palkkapohjaan lisätään 26,44 % vakiosivukuluja, minkä jälkeen lasketaan flat rate 40 % sekä JTF:n 80 % ja Tulevaisuusrahaston 20 % osuudet. Toteutuneita kirjanpidon sivukuluja ei lisätä toiseen kertaan. Tarkista mahdollinen lomaraha ja muu tukikelvoton osuus palkkariveiltä. Laskennallinen rahoitus on arvio, ei maksatuspäätös.

Liiteaineistossa on 1682:lle kirjattuja ICT-menoja sekä 380 € saldoero kustannuspaikkojen välillä. Sovellus huomauttaa näistä. Selvitä mahdollinen siirtotosite kirjanpidosta.

## Tiedostot ja ylläpito

**Ilmastovisio.html** on valmis käyttöversio. Muokattava lähdekoodi on `dist/`-kansiossa. **LASKENTA.md** sisältää tarkat laskentasäännöt, tuontimuodot, rajoitteet ja paikallisen palvelimen vaihtoehtoisen käynnistysohjeen. **TESTIT.md** sisältää aineiston täsmäytyksen ja testauksen rajauksen.

Kehittäjälle: `python build.py` päivittää yhden tiedoston käyttöversion. `node --test tests/core.test.cjs` ajaa laskentatestit. Sovelluksen käyttö ei vaadi Pythonia tai Nodea. JSZipin lisenssi on `dist/vendor/`-kansiossa. GitHub-julkaisua ei ole tehty. Pidä omat pääkirjat ja varmuuskopiot lähdekoodikansion ulkopuolella.

Automaattiset laskenta- ja sovelluslogiikkatestit on ajettu. Oikean selaimen visuaalista tarkistusta tai kaikkien selainten paikallisen tallennuksen yhteensopivuutta ei ole tässä ympäristössä varmennettu.
