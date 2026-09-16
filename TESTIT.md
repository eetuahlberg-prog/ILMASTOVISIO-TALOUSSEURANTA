# Testaus ja täsmäytys

Testattu 16.9.2026. Lähdeaineisto: Ilmastovisio_paakirjat_06-08_2026(1).xlsx. Alkuperäistä pääkirjaa ei ole mukana projektipaketissa. Tämä raportti sisältää aineistosta johdettuja yhteissummia, ja se on rajattu Git-seurannan ulkopuolelle.

## Tositerivien täsmäytys

Sovelluksen oma XLSX-lukija avasi kaikki kuusi välilehteä. Jokaisen välilehden tositerivien summa täsmäsi pääkirjan kustannuspaikan kuukausittaiseen yhteissummaan. Vertailu tehtiin myös erillisellä Python-laskennalla käyttäen desimaalilukuja, ilman sovelluksen tuonti- tai laskentalogiikkaa.

| Kuukausi | 1682, € | 1683, € | Menot yhteensä, € | Tositerivejä |
| --- | ---: | ---: | ---: | ---: |
| Kesäkuu 2026 | 8 422,36 | 1 771,39 | 10 193,75 | 17 |
| Heinäkuu 2026 | 7 824,53 | 1 777,93 | 9 602,46 | 19 |
| Elokuu 2026 | 9 341,96 | 1 357,43 | 10 699,39 | 16 |
| Yhteensä | 25 588,85 | 4 906,75 | 30 495,60 | 52 |

Ensituonti: 52 uutta, 0 ennestään. Uudelleentuonti: 0 uutta, 52 ennestään. Kokonaissumma pysyi samana. Tilien alku- ja loppusaldot, tilisummat, koko raportin summat ja Tunnisteet-rivit eivät kasvattaneet menoja.

## Rahoituslaskelman vertailuarvot

Seuraavat luvut ovat alustava laskentatesti, jossa kaikki tilin 5002 nettokirjaukset oletetaan tukikelpoiseksi palkkapohjaksi. Ne eivät osoita, että mahdollinen lomaraha tai muut tukikelvottomat erät olisi tarkistettu. Prosentit pyöristetään kuukausittain sentteihin.

| Erä | Kesäkuu, € | Heinäkuu, € | Elokuu, € | Yhteensä, € |
| --- | ---: | ---: | ---: | ---: |
| Palkkapohja | 7 031,86 | 6 215,40 | 7 482,32 | 20 729,58 |
| Vakiosivukulut 26,44 % | 1 859,22 | 1 643,35 | 1 978,33 | 5 480,90 |
| Palkkakustannukset, arvio | 8 891,08 | 7 858,75 | 9 460,65 | 26 210,48 |
| Flat rate 40 % | 3 556,43 | 3 143,50 | 3 784,26 | 10 484,19 |
| Kustannuspohja, arvio | 12 447,51 | 11 002,25 | 13 244,91 | 36 694,67 |
| JTF 80 %, arvio | 9 958,01 | 8 801,80 | 10 595,93 | 29 355,74 |
| Tulevaisuusrahasto 20 %, arvio | 2 489,50 | 2 200,45 | 2 648,98 | 7 338,93 |
| Flat rate − 1683:n menot | 1 785,04 | 1 365,57 | 2 426,83 | 5 577,44 |

Kustannuspaikan 1682 tilin 5403 tositerivejä on heinä- ja elokuussa yhteensä 760 €. Ne sisältyvät toteutuneisiin menoihin, mutta eivät automaattiseen palkkapohjaan. Kun nämäkin muut kulut huomioidaan flat rate -marginaalissa, marginaali on 4 817,44 €.

## Aineistosta löytynyt saldoero

Heinäkuun lopussa 1682/5403-saldo on 380 €, mutta elokuun alkusaldo on 0 €. Vastaavasti 1683/5403-saldo kasvaa heinäkuun loppusaldosta 682,68 € elokuun alkusaldoon 1 062,68 €. Tämä viittaa 380 € kustannuspaikkasiirtoon, jota ei näy toimitetun aineiston päivätyissä tositeriveissä.

Sovellus säilyttää tositerivien mukaisen jaon ja näyttää molemmat saldoerot. Se ei siirrä 380 € automaattisesti kustannuspaikkojen välillä eikä luo puuttuvaa tositetta. Hankkeen kokonaismenot eivät muutu tästä erotuksesta, mutta kustannuspaikkajako ja 1683-pohjainen marginaali vaativat kirjanpidon tarkistuksen.

## Automaattitestit

Mukana on 15 Node-testiä: suomalaiset rahamäärät ja päivämäärät, vakiosivukulujen laskenta, ICT:n poissulku palkkapohjasta, kredit-oikaisut ja symmetrinen senttipyöristys, palkkapohjan tarkistus, uudelleentuonti, ristiriitainen tosite, rivinumeroton tuonti ja samojen rivien lukumäärä, ryhmitelty pääkirja, summatäsmäytys, virheelliset rivit, CSV-lainaukset ja vientisuojaus, kuukausi-/vuosi-/hankesummien täsmäytys, ennuste, rahoituksen vaiheet, varmuuskopion validointi ja saldokatkokset. Kaikki läpäisivät testit.

Lisäksi sovelluksen toimintoja testattiin DOM-ympäristössä ja IndexedDB-emulaatiossa oikealla XLSX-tiedostolla:

- XLSX:n kuusi välilehteä luettiin sovelluksen varsinaisella lukijalla.
- Tuonnin esikatselu, tallennus ja toistettu tuonti onnistuivat.
- Tapahtumahaku ja palkkapohjan muutos tallentuivat.
- Rahoituserän haettu, päätetty ja saatu summa tallentuivat erikseen.
- Valmis kirjanpitokuukausi käynnisti ennusteen.
- Raporttinäkymät ja vientitoiminnot toimivat.
- Varmuuskopio palautti 52 tositeriviä ja testissä lisätyn rahoituserän koko aineiston tyhjennyksen jälkeen.
- Vääränmuotoinen varmuuskopio hylättiin muuttamatta tietoja.
- Samanaikaisesti toisessa välilehdessä muuttuneiden tietojen päälle ei tallennettu.

## Testauksen rajaus

DOM- ja tietokantaemulaatio ei vastaa oikean selaimen visuaalista tai file://-tallennustestiä. Selainten todellista paikallisen tiedoston tallennuskäyttäytymistä, käyttöliittymän renderöintiä eri näytöillä tai latausvalintaikkunoita ei ole tässä ympäristössä varmennettu. Vientiä, palautusta ja tallennusta kannattaa kokeilla omassa selaimessa ensimmäisen käyttökerran yhteydessä.

Ennuste on yksinkertainen kuukausivauhtiarvio, ei hyväksytty maksatusennuste. Palkkojen tukikelpoisuus, mahdollinen lomarahaosuus, päätösten ehdot sekä 380 € siirtotosite jäävät käyttäjän ja kirjanpidon tarkistettaviksi.
