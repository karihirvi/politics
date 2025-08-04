# CLAUDE.md

Tämän repositorion tarkoitus on tarjota kattava järjestelmä tehokkaaseen poliittiseen 
viestintään Suomen kontekstissa, erityisesti Perussuomalaisten (PS) puolueelle. Se sisältää 
näkemyksiä eri poliittisen viestinnän, psykologian ja kulttuuritutkimuksen asiantuntijoilta.

## Päätavoite
Tuottaa iteratiivisesti tekstuaalista sosiaalisen median sisältöä, joka resonoi suomalaisten äänestäjien kanssa.

## Sisällöntuotantoprosessi

Järjestelmä luo tehokkaita yksittäisiä postauksia sosiaaliseen mediaan:

**Organisointi:**
- Kaikki postaukset luodaan `postaukset`-kansioon
- Jokainen postausaihe saa oman kansion: `p###-aiheen-nimi`
  - p = postaus
  - ### = Kolminumeroinen numero (001, 002, jne.)
  - aiheen-nimi = Käyttäjän valitsema kuvaava nimi (pienet kirjaimet, väliviivat)

**Tiedostorakenne:**
- Seuraa A-B iteraatiokuviota:
  - **A-tiedostot**: Käyttäjän ohjeet (esim. `p001-01-a-ohjeet.md`)
  - **B-tiedostot**: Clauden vastaus (esim. `p001-01-b-vastaus.md`)
- Jatka 02-a, 02-b hienosäätöjä varten

**Esimerkkigerakenne:**
```
postaukset/
├── p001-burkakielto-jatko/
│   ├── p001-01-a-ohjeet.md
│   ├── p001-01-b-burkakielto-paastaustyyli.md
│   ├── p001-02-a-ohjeet.md
│   └── p001-02-b-muokattu-versio.md
```

### Nimeämiskäytäntö

**Kaikki pienillä kirjaimilla läpi:**
- Postauskansiot: `p###-aiheen-nimi/`
- Sisällä olevat tiedostot: `p###-##-a-kuvaus.md` ja `p###-##-b-kuvaus.md`
  - `p###` = Postauksen numero (esim. p001, p002)
  - `##` = Iteraationumero (01, 02, 03...)
  - `a` = Käyttäjän luoma sisältö (pyynnöt, palaute)
  - `b` = Clauden generoima sisältö (vastaukset)
  - `kuvaus` = Lyhyt kuvaus sisällöstä
- Aiheet: pienet kirjaimet väliviivoilla (esim. `burkakielto-jatko`)

ERITTÄIN TÄRKEÄÄ:
- Säilytä aina johdonmukainen pienten kirjaimien käyttö
- Älä koskaan muokkaa olemassa olevia tiedostoja - luo uusia iteraatioita
- **Nykyinen versioseäntö**: Viimeisin generoitu tiedosto (korkein numero) on aktiivinen versio
  - Esim. jos sekä p001-01-b että p001-02-b ovat olemassa, käytä p001-02-b
  - Käyttäjä mainitsee erikseen mahdolliset poikkeukset tähän sääntöön

### Sisällöntuotannon ohjeistus

1. **Uutta postausta luotaessa**
   - Luo automaattisesti ensimmäinen pyyntömalli: `p###-01-a-pyyntö.md`
   - Käytä vakiomallia osioilla Tavoite, Tyyli, Pituus, Keskeiset kohdat, jne.
   - Tämä säästää käyttäjän aikaa ja varmistaa yhtenäisen rakenteen

2. **Kun käyttäjä sanoo "käsittele"**
   - Käsittele pyyntötiedosto generoidaksesi vastauksen
   - **TÄRKEÄÄ**: Luo automaattisesti seuraava palautemalli vastauksen generoinnin jälkeen
   - Tämä varmistaa sujuvan iteraatiotyökulun

3. **Kun käyttäjä antaa muita ohjeita**
   - Jos rajoitteet ovat epäselviä, pyydä tarkennusta
   - Jos on useita päteviä tulkintoja, tarjoa useita vaihtoehtoja
   - Viittaa taustamateriaaleihin ohjeiden mukaan (puolueohjelmat, kehystystekniikat, tyylesimerkit)

4. **Vastausmuoto**
   - Useille vaihtoehdoille: Luo kaikki variaatiot yhteen B-tiedostoon, selvästi eroteltuina
   - Käytä kuvaavia otsikoita jokaiselle versiolle
   - Pidä suomenkielinen teksti erillään ohjeista/kommenteista

5. **Palautteen käsittely**
   - **KRIITTINEN**: Kun käyttäjä antaa palautetta mistä tahansa osasta, sovella sitä globaalisti
   - Jos käyttäjä korjaa kirjoitusasun (esim. "burkkaa" → "burkaa"), korjaa se kaikkialla
   - Jos käyttäjä ehdottaa sävyn muutosta yhdessä postauksessa, harkitse koskeeko se muita
   - Jos käyttäjä mainitsee puuttuvan kontekstin, lisää konteksti KAIKKIIN postauksiin, ei vain kommentoituun
   - Ajattele aina: "Koskeeko tämä palaute muualle?"

### Työnkulkuesimerkki

**Vaihe 1: Käyttäjä luo pyyntötiedoston**
```
postaukset/p002-tuulivoimakritiikki/p002-01-a-pyyntö.md:

# Pyyntö: Tuulivoimakritiikin postaus

Tavoite: Paljastaa tuulivoimatukien piilotetut kustannukset
Tyyli: Analyyttinen - haluan rakentaa uskottavuutta faktoilla
Pituus: KESKIPITKÄ (5-6 kappaletta)
Keskeiset kohdat:
- Veronmaksajien taakka
- Tuulivoiman epäluotettavuus
- Vaikutus sähkön hintaan

Sisällytä uskottavia lähteitä (muista: ei Wikipediaa)
```

**Vaihe 2: Claude generoi vastauksen**
```
postaukset/p002-tuulivoimakritiikki/p002-01-b-tuulivoiman-todelliset-kustannukset.md:

# Tuulivoiman todelliset kustannukset paljastuvat

[Analyyttisen tyylin postaus 5-6 kappaleella, faktoja, lähteitä...]

Lähteet:
1. Energiavirasto (2023): https://energiavirasto.fi/...
2. VTT:n tutkimus (2024): https://www.vtt.fi/...
```

**Vaihe 3: Käyttäjä antaa palautetta**
```
postaukset/p002-tuulivoimakritiikki/p002-02-a-palaute.md:

Hyvä alku, mutta:
- Lisää emotionaalinen koukku alkuun
- Sisällytä vertailu ydinvoiman kustannuksiin
- Sävy on liian akateeminen, tee siitä helpommin lähestyttävä
```

**Vaihe 4: Claude luo hienosäädetyn version**
```
postaukset/p002-tuulivoimakritiikki/p002-02-b-tuulivoiman-piilotetut-kulut.md:

[Hienosäädetty versio, joka sisältää kaiken palautteen]
```

## Taustatiedot

Tekstin kirjoittamiseen voit käyttää taustatietoja ja muita resursseja:
- **puolueohjelmat** - sisältää eri poliittisten puolueiden viralliset ohjelmat
- **kehystys** - sisältää tietoa kehystystekniikoista
- **resurssit** - sisältää esimerkkejä ja muita materiaaleja
- **tyyliesimerkit** - sisältää valikoituja esimerkkejä aiemmista postauksista, joita voit käyttää inspiraationa tai viitteenä.
  Esimerkit on valittu niiden arvioidun tehokkuuden perusteella suomalaisessa poliittisessa viestinnässä. Ne on numeroitu 
  helppoa viittausta varten, esim. e001-..., e002-... jne. Etuliite "e" tarkoittaa "esimerkki" (example), jotta Claude 
  tunnistaa ne helposti. Postauksia postaukset/- tai campaigns/-kansioista voidaan nostaa tähän kansioon, jos niitä pidetään erityisen tehokkaina.

## Tyyli- ja tavoiteoppaat

### Tyyliopas
Kattava tyyliopas tehokkaaseen poliittiseen sisällöntuotantoon:
- **CLAUDE_TYYLI.md** - Suomenkielinen tyyliopas 7 erilaisella kirjoitustyylillä

### Tyylinvalintaopas
Opas oikean tyylin valintaan postauksillesi:
- **CLAUDE_TAVOITE.md** - Suomenkielinen opas tyylin valintaan

Tämä opas auttaa valitsemaan tehokkaimman tyylin viestintätavoitteellesi.

### Hienojakoiset rajoiteasiakirjat
Kolme yksityiskohtaisten rajoitteiden tasoa sisällöntuotannon optimointiin:

#### Syntaktiset rajoitteet
- **CLAUDE_SYNTAKSI.md** - Kieliopilliset rajoitteet tyyleittäin (lausetyypit, pituudet, rakenteet)

#### Retoriset rajoitteet
- **CLAUDE_RETORIIKKA.md** - Argumentaatiorakenteet ja retoriset keinot tyyleittäin

#### Leksikaaliset rajoitteet
- **CLAUDE_SANASTO.md** - Sanasto, rekisterit ja fraseologia tyyleittäin

### Postausten kirjoitusopas
Yksityiskohtaiset ohjeet yksittäisten postausten luomiseen:
- **CLAUDE_POSTAUS.md** - Suomenkielinen opas yksittäisten postausten kirjoittamiseen

### Nyanssien opetussysteemi
Opettaa Claudelle tekstin hienovaraisia vivahteita ja "kulmia":
- **CLAUDE_NYANSSIT.md** - Ohje nyanssien oppimiseen ja opettamiseen
- **nyanssit/** - Kansio oppimateriaalille ja analyyseille

### Oppaiden käyttö
1. Käyttäjä kuvaa viestintätavoitteensa
2. Claude tunnistaa sopivimman tyylin/tyylit
3. Sisältö luodaan tyyliominaisuuksia noudattaen
4. Esimerkkitiedostot (e###) toimivat konkreettisina viitteinä

### 7 poliittisen viestinnän tyyliä
1. **Paasaustyyli** - Tunteellinen, käskevä, mobilisoiva
2. **Analyyttinen** - Strateginen, kouluttava, legitimoiva
3. **Konseptuaalinen** - Esittelee uusia ideoita ja viitekehyksiä
4. **Argumentoiva** - Looginen, kumoaa vastapuolen väitteitä
5. **Kriittis-poliittinen** - Kritisoi vastustajia, skandaalit
6. **Filosofis-uskonnollinen** - Arvot, merkitys, perinteet
7. **Populistinen** - Yksinkertaiset ratkaisut, taloudelliset vetoomukset


## Kieliohjeistus
- Postausten kieli on **suomi**, joten sinun tulee kirjoittaa postaukset suomeksi
- Jos tarvitset apua suomen kanssa, kysy käyttäjältä
- Englantia käytetään käyttäjän ohjeisiin ja muihin ohjeistuksiin tarvittaessa
- ÄLÄ KOSKAAN käytä hashtageja postauksissa
- Postausten pituusohjeistukseen viittaa tyyliesimerkit tyypillisille pituuksille

## Lähde- ja viittausohjeistus
- **KAIKKI viittaukset tulee olla URL-osoitteita**: Älä koskaan käytä epämääräisiä viittauksia kuten "Tutkimus osoittaa" tai "Raportti sanoo"
- **Kielivaatimus**: Lähteiden tulee olla vain suomeksi tai englanniksi
- **Uskottavuusvaatimus**: 
  - Älä koskaan käytä Wikipediaa lähteenä
  - Käytä vain yleisesti uskottavia lähteitä kuten:
    - Hallituksen verkkosivut (.gov, .fi ministeriöt)
    - Vakiintuneet uutisorganisaatiot (YLE, HS, BBC, Reuters)
    - Akateemiset laitokset ja tutkimuslaitokset
    - Viralliset kansalaisjärjestöjen ja kansainvälisten järjestöjen verkkosivut
    - Vertaisarvioidut julkaisut ja viralliset raportit
- **Muoto**: JOKAISELLA POSTAUKSELLA tulee olla oma lähdeluettelo
  - Sijoita kaikki viitteet JOKAISEN yksittäisen postauksen LOPPUUN
  - Käytä hakasulkeita [1] tai sulkeita (1) tekstissä viittausten merkitsemiseen
  - Älä koskaan käytä ylä- tai alaindeksinumeroita
  - Listaa täydet URL-osoitteet alhaalla kohdassa "Lähteet:" tai "Viitteet:"
  - Älä koskaan jaa lähdeluetteloita postausten välillä - jokainen postaus on itsenäinen
- **TÄRKEÄÄ**: Generoidessasi sisältöä URL-osoitteilla, käytä WebFetch-työkalua varmistaaksesi linkkien toimivuuden
  - Jos URL ei toimi, etsi vaihtoehtoisia lähteitä
  - Älä koskaan sisällytä rikkinäisiä tai kuvitteellisia URL-osoitteita
- **Esimerkkimuoto**:
  ```
  Ranskan sisäministeriön mukaan [1] burkakielto on vähentänyt turvallisuusongelmia.
  
  Lähteet:
  1. Ranskan sisäministeriön raportti (2019): https://www.interieur.gouv.fr/...
  ```

## Keskeiset muistutukset
- Noudata iteratiivista prosessia huolellisesti
- Käytä versionumerointia johdonmukaisesti
- Pidä postaukset-kansio järjestyksessä
- Hyödynnä taustamateriaaleja tehokkaasti
- Varmista, että viestit resonoivat suomalaisen yleisön kanssa

## Tekniset yksityiskohdat
- Maksimi rivin pituus: 120 merkkiä
- **Markdown-muotoilu**: Käytä aina oikeaa markdown-syntaksia
  - Listojen tulee käyttää `-` tai `*` jokaisen kohdan alussa
  - Lihavoitu teksti `**teksti**`
  - Otsikot sopivilla `#`-tasoilla
  - Asianmukaiset rivinvaihdot osioiden välillä
- **Git commit -viestit**: Aina englanniksi