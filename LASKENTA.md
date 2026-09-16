# Ilmastovisio: talousseuranta v1

Yksityinen, paikallinen talousseurantatyökalu hankkeelle J11721. Käyttö ei edellytä asennuksia, tunnuksia, internetyhteyttä tai omaa backend-palvelinta.

## Käynnistä

1. Pura ZIP-paketti pysyvään kansioon omalle koneelle.
2. Avaa **Ilmastovisio.html** selaimessa. Käytä ajantasaista Chromea, Edgeä tai Firefoxia tavallisessa selainikkunassa.
3. Avaa **Pääkirjan tuonti**, valitse omat XLSX- tai CSV-pääkirjasi, tarkista esikatselu ja paina **Tallenna tuonti**.
4. Tarkista palkkapohja **Tapahtumat**-näkymässä. Aseta **Asetukset**-näkymässä viimeinen kokonaan kirjattu kuukausi, kun molempien kustannuspaikkojen aineisto on valmis.
5. Kirjaa maksatushakemukset ja niiden päätökset sekä maksut **Rahoitus**-näkymässä. Vie säännöllisesti JSON-varmuuskopio.

Sovellus avautuu ilman pääkirja- tai rahoitustapahtumia. Hankesuunnitelman budjetti ja laskentasäännöt ovat valmiina. Liitteitä ei ole sisällytetty sovellukseen tai projektikoodiin.

## Tallennus ja yksityisyys

Tiedot tallennetaan IndexedDB-tietokantaan käytettävän selaimen profiilissa. Sovellus ei tee verkkopyyntöjä. XLSX-lukijan tarvitsema JSZip on mukana paketissa. Fontit ovat järjestelmäfontteja. Ei analytiikkaa, CDN-latauksia, pilvitietokantaa, kirjautumista tai palvelinpuolen talouskäsittelyä. Content Security Policy estää connect-src-verkkoyhteydet ja ulkoiset resurssit.

Selaimen tietojen poistaminen voi poistaa myös taloustiedot. Selain, profiili, tiedostopolku tai osoite voi vaikuttaa tallennustilaan. Pidä käyttämäsi HTML samassa paikassa. Vie varmuuskopio ennen tiedoston siirtämistä, päivitystä tai selainvaihtoa ja palauta se tarvittaessa. JSON sisältää luottamuksellisia tietoja, eikä se ole salattu. Laite ja selainprofiili on suojattava normaalisti. Yksityinen selaus ei sovi pysyvään seurantaan.

Jos paikallisen tiedoston tallennus on selaimen käytännöissä estetty, sovellus näyttää virheen eikä teeskentele tallentaneensa tietoja. Vaihtoehtona voi käyttää pelkästään staattisia tiedostoja tarjoavaa paikallista palvelinta: suorita projektikansiossa `python -m http.server 8765 --bind 127.0.0.1 --directory dist` ja avaa `http://127.0.0.1:8765`. Tämä ei sisällä backend-logiikkaa eikä lähetä talousaineistoa verkkoon. Pidä osoite samana jatkossa.

## Tuonti

XLSX-tuonti lukee kaikki ei-tyhjät välilehdet. Liitteen maakuntaliiton ryhmitelty pääkirja on tuettu: kustannuspaikka ja tilinumero luetaan ryhmäotsikoista, vain päivätyt tositerivit tuodaan. Alkusaldo, loppusaldo, Tunnisteet ja Yhteensä-rivit eivät ole menoja. Tositerivien summat täsmäytetään kustannuspaikan raporttisummaan. Tiedosto voi olla enintään 25 Mt. Vanha binäärinen XLS ei ole tuettu; tallenna se ensin XLSX-muotoon.

Tavallisessa taulukossa käytetään sarakkeita `Päivämäärä`, `Kustannuspaikka`, `Tili`, `Tilin nimi`, `Tosite`, `Selite`, `Debet`, `Kredit`. Sarakkeet `Jnro` ja `Tl` ovat valinnaiset mutta suositeltavat. Sovelluksesta saa tyhjän CSV-pohjan. CSV tukee puolipistettä, pilkkua ja sarkainta, lainattuja kenttiä, suomalaisia desimaaleja sekä UTF-8- ja Windows-1252-merkistöä. Excelin päivämääräsolut, jaettu teksti, upotettu teksti sekä 1900/1904-päivämääräjärjestelmät on huomioitu. Kaavan välimuistiarvon puuttuminen estää tuonnin.

Tuonti näyttää uudet, aiemmin löytyneet ja muiden kustannuspaikkojen ohitetut rivit. Virhe tai ristiriita estää koko tuontierän tallentamisen. Muiden kuin tuettujen sarakerakenteiden kohdalla näytetään virhe; v1 ei sisällä vapaata sarakkeiden kohdistuseditoria.

Rivin tunnistus perustuu päivämäärään, kustannuspaikkaan, tiliin, tositteeseen ja Jnroon. Tiedoston nimeä tai välilehden nimeä ei käytetä tunnisteena. Tositteiden ja rivinumeroiden etunollat normalisoidaan tunnistuksessa. Ilman Jnroa verrataan myös summia ja selitettä sekä samojen rivien esiintymiskertoja. Myös rivinumeroton CSV voidaan tunnistaa aiemmin tuodusta XLSX:stä. Ilman yksilöllistä rivinumeroa kahta täysin samanlaista eri kirjausta ei voi varmasti erottaa uusintatuonnista. Säilytä Jnro ja johdonmukainen vientitapa. Muuttunut summa tai selite saman tunnisteen rivillä näytetään ristiriitana eikä aiempaa tietoa korvata automaattisesti.

Käsin lisätyille riveille käytetään samaa tunnistusta. Poistetun rivin voi tuoda myöhemmin uudelleen. Palkkapohjan rajaus kannattaa siksi tehdä tarkistusmäärällä, ei kirjanpitorivin poistolla.

## Laskenta

Kaikki rahamäärät käsitellään kokonaislukusentteinä. Prosentit pyöristetään kuukausittain sentteihin; vuosi- ja hankesummat ovat kuukausisummien summia. Maksatusjakson tai EURA-järjestelmän pyöristystapa voi tuottaa senttieroa.

- Kirjanpidon menot = debet − kredit kustannuspaikoilta 1682 ja 1683. Kuluiksi luetaan tilit 4000–8999. Tase- ja tulotilit näkyvät tapahtumissa mutta eivät menoina; niistä huomautetaan.
- Palkkapohja = kustannuspaikan 1682 tilin 5002 nettokirjaukset tai käyttäjän tarkistamat palkkapohjan määrät. Palkkatilit ovat muutettavissa asetuksissa. Lomaraha ja tukikelvottomat osuudet pitää poistaa palkkapohjasta. Hankkeelle jo kohdistettua osa-aikaisen palkkaa ei kerrota 80 prosentilla toiseen kertaan.
- Vakiosivukulut = palkkapohja × 26,44 %. Ne sisältävät mallin mukaiset sivukulut ja lomarahan. Kirjanpidon toteutuneita sivukuluja ei lisätä tähän uudestaan.
- Hyväksyttävien palkkojen arvio = palkkapohja + vakiosivukulut.
- Flat rate = hyväksyttävien palkkojen arvio × 40 %.
- Hyväksyttävä kustannuspohja, arvio = palkkakustannukset + flat rate.
- JTF = kustannuspohja × 80 %. Tulevaisuusrahasto = kustannuspohja − JTF, eli 20 % pyöristysero huomioiden.
- Flat rate -marginaali = flat rate − 1683:n todelliset menot. Erillinen lisäluku vähentää myös 1682:lle kirjatut muut kuin palkka- ja sivukulut.

Budjetin käyttöastetta ja jäljellä olevaa budjettia verrataan laskennalliseen kustannuspohjaan. Kirjanpidon menojen osuus budjetista näytetään rinnalla. JTF:n ja Tulevaisuusrahaston suunnitelmamäärät säilytetään täsmälleen asiakirjan mukaisina; ohjelma huomauttaa niiden ylittämisestä mutta ei leikkaa laskennallista arviota automaattisesti.

Pääkirja ei todista maksua työntekijälle, palkkaerän tarkkaa koostumusta, lomapalkan ansaintajaksoa tai tukikelpoisuutta. Summat ovat maksatuksen valmistelua tukevia arvioita, eivät rahoittajan hyväksyntä. Palkkapohjan tarkistus ja perustelu säilyvät varmuuskopiossa, alkuperäinen kirjanpitosumma ei muutu.

## Rahoitus ja ennuste

Yksi rahoitustapahtuma sisältää saman rahoittajan yhden maksatusjakson haetun, päätetyn ja saadun yhteissumman. Päivitä samaa tapahtumaa, älä lisää sen eri vaiheita erillisiksi eriksi. Tyhjä summa tarkoittaa puuttuvaa vaihetta; 0 € tarkoittaa kirjattua nollamäärää, esimerkiksi hylkäystä. Osamaksujen saatu summa on kumulatiivinen ja maksupäivä viimeisin. V1 ei sisällä erillistä osamaksutapahtumien taulukkoa, joten erittely tallennetaan lisätietoon.

Laskennallisesti vielä haettavana = enintään nollaan alhaalta rajattu laskennallinen osuus − haettu. Laskennallisesti saamatta = laskennallinen osuus − saatu, alaraja nolla. Päätetty mutta maksamatta lasketaan rahoituserittäin. Hylätyn osuuden mahdollista uudelleenhakua ei päätellä automaattisesti. Rahoituksen yhteenveto näyttää kaikki kirjatut jaksot myös silloin, kun menojen katkaisukuukausi on asetettu. Hankkeen yleistä rahoituspäätöstä ei kirjata maksatuseräksi.

Ennuste edellyttää käyttäjän vahvistamaa viimeistä kokonaan kirjattua kuukautta. Menojen loppuennuste = toteuma + jäljellä olevat hankekuukaudet × viimeisten enintään kolmen valmiin kuukauden keskiarvo. Myös nollakuukaudet ovat mukana. Vaihtoehtoinen oma menoarvio €/kk korvaa menojen keskiarvon, mutta kustannuspohjan ennuste käyttää edelleen toteuman keskiarvoa. Ennuste ei huomioi automaattisesti tulevia hankintoja, palkankorotuksia eikä ilmastokoordinaattorin päättymistä maaliskuussa 2028. Se ei ole kassavirtaennuste.

## Aineistohavainnot

Hankeaika: 1.6.2026–31.5.2028. Budjetti 309 896 €, palkat 221 354 €, flat rate 88 542 €, JTF 247 916 €, Tulevaisuusrahasto 61 980 €. Lähde: hyväksytty hankesuunnitelma 31.3.2026, sivut 2, 17, 26–27, 32–36. Sivulla 17 vahvistetaan Tulevaisuusrahaston omarahoitusosuus. Erillistä JTF:n tai Tulevaisuusrahaston rahoituspäätöstä ei ollut toimitetuissa liitteissä.

Tosiasiallisten palkkojen vakiosivukulumallin tulkintaa tarkistettiin myös rahoittajan julkisesta [19.5.2026 hakuinfosta, sivut 4–8](https://rakennerahastot.fi/documents/91635434/258106329/Hakuinfo%2019.5.2026%20Kustannusmalli%20Flat%20rate%2040%20%25%2C%20tosiasialliset%20palkkakustannukset%20ja%20palkkakustannusten%20yksikk%C3%B6kustannus.pdf/d56b30df-e7a2-472f-03ab-4d9c74d82231?t=1779192185416). Tämä on yleisohje, eikä se korvaa hankkeen omaa rahoituspäätöstä.

Toimitetun pääkirjan 1682 sisältää myös ICT-menoja. Heinäkuun lopun ja elokuun alun välillä tilillä 5403 on vastakkaiset 380 € saldoerot kustannuspaikkojen välillä. Sovellus näyttää erot eikä muodosta tositetta niiden perusteella. Selvitä kirjanpidosta mahdollinen siirtotosite. Yksityiskohtaiset vertailut ovat tiedostossa TESTIT.md.

## Projektin ylläpito

`dist/index.html`, `dist/style.css`, `dist/app.js`, `dist/core.js` ja `dist/xlsx-reader.js` ovat muokattavat lähdetiedostot. `dist/vendor` sisältää JSZipin ja sen lisenssin. **Ilmastovisio.html** on samoista lähteistä koottu yhden tiedoston käyttöversio. Päivitä se muutosten jälkeen komennolla `python build.py`. Käyttö ei vaadi Pythonia tai Nodea.

Laskennan ja tuonnin automaattitestit: `node --test tests/core.test.cjs` (Node 18+). Sovellus ei tarvitse npm-riippuvuuksien asennusta. Mukana oleva `.gitignore` estää tavallisten pääkirja- ja varmuuskopiotiedostojen tahattoman lisäämisen Gitiin. Älä silti sijoita omia talousaineistojasi lähdekoodikansioon. GitHub-julkaisua ei ole tehty.

Raportit voi viedä CSV-muodossa Exceliin. V1 ei kirjoita XLSX-raporttia, koska CSV-vienti täyttää tämän version vientitarpeen. Koko aineiston vienti ja palautus käyttää version 1 JSON-muotoa. Virheellinen varmuuskopio hylätään ennen nykyisten tietojen korvaamista. Samanaikainen tallennus vanhentuneesta välilehdestä estetään.

Automaattiset laskenta- ja sovelluslogiikkatestit on ajettu. Oikean selaimen visuaalista testiä tai kaikkien selainten file://-tallennusyhteensopivuutta ei ole tässä ympäristössä varmennettu.
