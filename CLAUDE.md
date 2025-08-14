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
  - **A-tiedostot**: Käyttäjän pyynnöt ja palautteet (esim. `p001-01-a-pyyntö.md`)
    - Sisältää tavoitteet, rajoitteet ja raakatekstin
    - Tyyli, pituus, sävy
    - Ydinviestit ja konkreettiset esimerkit
  - **B-tiedostot**: Clauden generoimat postaukset (esim. `p001-01-b-vastaus.md`)
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

### Sisällöntuotannon prosessi

#### 1. Pyynnön luominen (käyttäjä)

Käyttäjä luo a-tiedoston, joka sisältää:
- **Tavoitteet ja rajoitteet** - mitä halutaan saavuttaa
- **Tyyli ja pituus** - valittu tyyli 7:stä vaihtoehdosta
- **Raakateksti/ydinviestit** - mitä halutaan sanoa
- **Konkreettiset esimerkit** - tunnistettavia tilanteita

**SUOSITUS**: Käytä valmiita pyyntöpohjia:
1. **Täysi pyyntöpohja** `resurssit/tyokalut/pyyntopohja-malli.md`
   - Pohja huomioi kaikki CLAUDE_*.md ohjeissa määritellyt elementit
   - Sisältää valintaruudut, kehystämisen, retoriset tekniikat
   - Ohjaa automaattisesti p004-periaatteisiin (konkretiaa, tunnetta)
2. **Muotoilupyyntö** `resurssit/tyokalut/muotoilupyynto-malli.md`
   - Kun sinulla on valmis raakateksti
   - Haluaa vain visuaalista muotoilua (otsikot, kappaleet)
   - Korjaa kirjoitusvirheet, EI muuta sisältöä

Esimerkki (yksinkertainen pyyntö):
```markdown
# Pyyntö: [Aihe]

## Tavoite
Paljastaa ristiriita X:n ja Y:n välillä

## Tyyli
Kriittis-poliittinen, maltillinen sävy

## Pituus
KESKIPITKÄ (5-6 kappaletta)

## Ydinviestit
- Feministit vastustavat länsimaista seksismiä
- Samat tahot vaikenevat burkasta
- Tämä on kaksinaismoralismia

## Konkreettiset esimerkit
- #metoo-liike
- Bikinimainos vs burka
- Työpaikkaseksismi
```

#### 2. Postauksen generointi (Claude)

Claude:
1. Lukee a-tiedoston pyynnön
2. Muotoilee raakatekstin tehokkaaksi postaukseksi
3. Säilyttää käyttäjän ydinviestit
4. Lisää retorista voimaa ja tunnetta
5. Pitää kielen yksinkertaisena ja iskevänä
6. Luo b-tiedoston

#### 3. Palautteen käsittely

Käyttäjä antaa palautetta normaalisti (ei komentoja):
- "Liian pitkä, tiivistä 40%"
- "Vaihda tämä esimerkki parempaan"
- "Lisää konkretiaa tähän kohtaan"

Claude soveltaa palautetta globaalisti:
- Jos käyttäjä korjaa kirjoitusasun, korjaa kaikkialla
- Jos sävy muuttuu, harkitse koskeeko muita kohtia
- Ajattele: "Koskeeko tämä palaute muualle?"

#### 4. Vaihtoehtoisesti: Muotoilupyynnön käyttö

Jos käyttäjällä on valmis raakateksti, joka tarvitsee vain muotoilua:
1. Käytä **muotoilupyyntö-mallia** (`resurssit/tyokalut/muotoilupyynto-malli.md`)
2. Claude EI muuta sisältöä, vain:
   - Parantaa visuaalista ulkoasua (otsikot, kappaleet, listat)
   - Korjaa kirjoitusvirheet ja kielioppivirheet
   - Säilyttää kaikki argumentit ja viitteet
3. Sopii tilanteisiin, joissa sisältö on valmis mutta kaipaa selkeämpää rakennetta

#### TÄRKEÄÄ: Ennen postausten tekemistä

**Kun käyttäjä sanoo "lue muistiin" tai "lataa ohjeet":**
- Lue KAIKKI seuraavat CLAUDE_*.md tiedostot kontekstiisi tässä järjestyksessä:
  1. CLAUDE_NYANSSIT.md - Analyysit mikä toimii (erityisesti p004-vs-p005)
  2. CLAUDE_TYYLI.md - 7 tyylin määrittelyt
  3. CLAUDE_POSTAUS.md - Käytännön kirjoitusohjeet  
  4. CLAUDE_TAVOITE.md - Tyylin valintaopas
  5. CLAUDE_RETORIIKKA.md - Argumentaatiorakenteet
  6. CLAUDE_SYNTAKSI.md - Kieliopilliset rajoitteet
  7. CLAUDE_SANASTO.md - Sanastolliset rajoitteet
- Lue KAIKKI tiedostot, ei vain "tarvittaessa"
- Vahvista käyttäjälle: "Ohjeet luettu muistiin. Valmis luomaan postauksia."
- Tämä varmistaa, että kaikki tyyliohjeet ja rajoitteet ovat käytössä

### Työnkulkuesimerkki (p004-tyylinen)

**Vaihe 1: Käyttäjä luo pyynnön**
```
Käyttäjä: Teen postauksen feminismistä ja burkasta. 
Pitää paljastaa kaksinaismoralismi.
Feministit vastustavat länsimaista seksismiä mutta 
vaikenevat islamista.

[Käyttäjä kirjoittaa p006-01-a-pyyntö.md tiedoston]
```

**Vaihe 2: Claude generoi postauksen**
```
Claude: Luen pyynnön ja luon postauksen joka:
- Alkaa konkreettisella #metoo-viittauksella
- Rakentaa kontrastin bikini vs burka
- Käyttää tunnekielikuvia ("kangaspussi")
- Päättyy haasteeseen lukijalle

[Claude luo p006-01-b-kaksinaismoralismi.md]
```

**Vaihe 3: Käyttäjä antaa palautetta**
```
Käyttäjä: Hyvä perus mutta liian pitkä. 
Tiivistä 40% ja lisää konkreettinen esimerkki 
suomalaisesta kontekstista.

[Käyttäjä kirjoittaa p006-02-a-palaute.md]
```

**Vaihe 4: Claude tekee korjauksen**
```
Claude: Tiivistän tekstin ja lisään esimerkin 
suomalaisesta koulusta tai työpaikasta.

[Claude luo p006-02-b-kaksinaismoralismi-tiivistetty.md]
```

## Taustatiedot

Tekstin kirjoittamiseen voit käyttää taustatietoja ja muita resursseja:
- **puolueohjelmat** - sisältää eri poliittisten puolueiden viralliset ohjelmat
- **resurssit** - sisältää kaikki viestintämateriaalit järjestettynä alakansioihin:
  - **resurssit/tyokalut/** - Käytännön työkalut (pyyntopohja-malli.md, muotoilupyynto-malli.md, fraasit.md, esimerkit.md)
  - **resurssit/strategiat/** - Viestintästrategiat (narratiivit.md, retoriset-tekniikat.md, kehystys.md)
  - **resurssit/taustatiedot/** - Tieteelliset ja kontekstuaaliset taustat (arvot.md, puolueet.md, suomalainen_konteksti.md, tekniikat.md)
  - **resurssit/oppaat/** - PDF-muotoisia oppaita viestintätekniikkoihin (esim. kehystysopas-1-1.pdf)
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
- **TÄRKEÄ OIKEINKIRJOITUS**: Käytä aina "burka", EI "burkka" (yksi k, ei kaksi)

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
- **TÄRKEÄÄ - Tiedostojärjestelmässä navigointi**:
  - Tarkista AINA ensin nykyinen työhakemisto `pwd`-komennolla ennen tiedostojen luomista tai siirtämistä
  - Käytä absoluuttisia polkuja epäselvissä tilanteissa
  - Vältä sekaannuksia suhteellisten polkujen kanssa